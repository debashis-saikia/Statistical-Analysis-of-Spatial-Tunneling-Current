import matplotlib.pyplot as plt
import corner

for degree in range(1, 3):

    print(f"\n--- Running Poisson MCMC for Degree {degree} ---")

    # --- Frequentist fit (used for initialization) ---
    model = PolynomialRegression2D(degree=degree)
    model.fit(x, y, z)

    # Convert log-current → counts (Poisson requirement)
    curr = np.exp(z)

    # --- Run MCMC ---
    samples_p = run_mcmc_poisson(
        x, y, curr,
        model.polynomial_model,
        degree,
        initial_beta=model.beta_hat
    )

    print("Samples shape:", samples.shape)
