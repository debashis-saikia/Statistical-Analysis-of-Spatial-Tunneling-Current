x = (x - np.mean(x)) / np.std(x)
y = (y - np.mean(y)) / np.std(y)

# Log-posterior (Poisson)
def log_posterior_poisson(theta, x, y, curr, model_func):

    beta = theta  # model parameters (no sigma in Poisson)

    # Reject bad parameters immediately
    if np.any(np.isnan(beta)) or np.any(np.isinf(beta)):
        return -np.inf

    if np.any(np.abs(beta) > 100):
        return -np.inf

    # Model prediction (log-rate)
    z_model = model_func(x, y, beta)

    # Prevent overflow in exponential
    z_model = np.clip(z_model, -50, 50)

    # Convert to Poisson rate λ
    lam = np.exp(z_model)

    # Numerical safety (avoid log(0))
    lam = np.clip(lam, 1e-10, 1e10)

    # Poisson log-likelihood
    return np.sum(curr * np.log(lam) - lam)
