import matplotlib.pyplot as plt
import corner

for degree in range(1, 3):

    print(f"\n--- Running Poisson MCMC for Degree {degree} ---")

    # --- Frequentist fit (used for initialization) ---
    model = PolynomialRegression2D(degree=degree)
    model.fit(x, y, z)

    # Convert log-current → counts (Poisson requirement)
    curr = np.exp(z)
    # Convert to counts
    curr = np.exp(z)
    counts = np.round(100 * curr / np.mean(curr)).astype(int)
    counts[counts < 0] = 0
    curr_counts = counts
    # --- Run MCMC ---
    samples_p = run_mcmc_poisson(
        x, y, curr_counts,
        model.polynomial_model,
        degree,
        initial_beta=model.beta_hat
    )

    print("Samples shape:", samples.shape)
