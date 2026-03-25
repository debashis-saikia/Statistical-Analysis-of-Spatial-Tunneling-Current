import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln


class PoissonRegression2D:

    def __init__(self, degree):
        self.degree = degree
        self.beta_hat = None

    # -----------------------------
    # Build polynomial design matrix
    # -----------------------------
    def build_design_matrix(self, x, y):
        terms = []
        for i in range(self.degree + 1):
            for j in range(self.degree + 1 - i):
                terms.append((x**i) * (y**j))
        return np.vstack(terms).T  # shape (N, k)

    # -----------------------------
    # Log-likelihood (stable)
    # -----------------------------
    def log_likelihood(self, beta, X, z):
        eta = X @ beta

        # prevent overflow
        eta = np.clip(eta, -50, 50)

        lam = np.exp(eta)
        lam = np.maximum(lam, 1e-12)

        if not np.all(np.isfinite(lam)):
            return -1e20  # penalize bad region

        return np.sum(z * np.log(lam) - lam - gammaln(z + 1))

    # -----------------------------
    # Gradient (stable)
    # -----------------------------
    def gradient(self, beta, X, z):
        eta = X @ beta
        eta = np.clip(eta, -50, 50)

        lam = np.exp(eta)

        grad = X.T @ (z - lam)

        return -grad  # minimize

    # -----------------------------
    # Objective
    # -----------------------------
    def objective(self, beta, X, z):
        val = -self.log_likelihood(beta, X, z)

        if not np.isfinite(val):
            return 1e20

        return val

    # -----------------------------
    # Fit model
    # -----------------------------
    def fit(self, x, y, z):

        # ---- sanity checks ----
        if np.any(z < 0):
            raise ValueError("Poisson data must be non-negative")
        if np.any(~np.isfinite(z)):
            raise ValueError("z contains NaN or inf")

        # ---- normalize inputs (CRITICAL) ----
        self.x_mean, self.x_std = x.mean(), x.std()
        self.y_mean, self.y_std = y.mean(), y.std()

        x_scaled = (x - self.x_mean) / (self.x_std + 1e-12)
        y_scaled = (y - self.y_mean) / (self.y_std + 1e-12)

        # ---- design matrix ----
        X = self.build_design_matrix(x_scaled, y_scaled)
        N, k = X.shape

        # ---- initialization ----
        beta_init = np.zeros(k)
        beta_init[0] = np.log(np.mean(z) + 1e-6)

        # ---- optimization ----
        result = minimize(
            self.objective,
            beta_init,
            args=(X, z),
            jac=self.gradient,
            method="L-BFGS-B"
        )

        if not result.success:
            print("⚠ Optimization warning:", result.message)

        self.beta_hat = result.x
        self.X = X
        self.z = z
        self.N = N
        self.k = k

        # ---- fitted values ----
        eta = X @ self.beta_hat
        eta = np.clip(eta, -50, 50)

        self.lam = np.exp(eta)

        # ---- log-likelihood ----
        self.logL = self.log_likelihood(self.beta_hat, X, z)

        # ---- deviance ----
        z_safe = np.where(z == 0, 1, z)

        self.deviance = 2 * np.sum(
            np.where(
                z > 0,
                z * np.log(z_safe / self.lam) - (z - self.lam),
                -self.lam
            )
        )

        self.deviance_red = self.deviance / (N - k)

        # ---- Pearson chi-square ----
        self.chi2 = np.sum((z - self.lam)**2 / self.lam)
        self.chi2_red = self.chi2 / (N - k)

        # ---- information criteria ----
        self.AIC = -2 * self.logL + 2 * k
        self.BIC = -2 * self.logL + k * np.log(N)

    # -----------------------------
    # Predict
    # -----------------------------
    def predict(self, x, y):

        x_scaled = (x - self.x_mean) / (self.x_std + 1e-12)
        y_scaled = (y - self.y_mean) / (self.y_std + 1e-12)

        X = self.build_design_matrix(x_scaled, y_scaled)

        eta = X @ self.beta_hat
        eta = np.clip(eta, -50, 50)

        return np.exp(eta)

    # -----------------------------
    # Summary
    # -----------------------------
    def summary(self):

        print("\nPoisson Regression (2D Polynomial GLM)\n")

        print(f"Degree: {self.degree}")
        print(f"Parameters: {self.k}")

        print("\n--- Coefficients ---")
        print(self.beta_hat)

        print("\n--- Fit Quality ---")
        print(f"Log-Likelihood: {self.logL:.6f}")

        print(f"Deviance: {self.deviance:.6f}")
        print(f"Reduced Deviance: {self.deviance_red:.6f}  <-- PRIMARY")

        print(f"Pearson Chi²: {self.chi2:.6f}")
        print(f"Reduced Chi²: {self.chi2_red:.6f}  <-- DISPERSION CHECK")

        print("\n--- Model Selection ---")
        print(f"AIC: {self.AIC:.6f}")
        print(f"BIC: {self.BIC:.6f}")