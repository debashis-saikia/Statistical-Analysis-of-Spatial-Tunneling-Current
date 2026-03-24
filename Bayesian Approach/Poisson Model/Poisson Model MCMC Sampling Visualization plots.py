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

    print("Samples shape:", samples_p.shape)

    k = samples_p.shape[1]   

    # --- Scatter plot (posterior relationship between parameters) ---
    plt.figure()
    plt.plot(samples_p[:, 0], samples_p[:, 1], 'k.', alpha=0.1)
    plt.title(f"Posterior Scatter (Degree {degree})")
    plt.xlabel("b0")
    plt.ylabel("b1")
    plt.show()


    # --- Trace plots (convergence check) ---
    fig, axes = plt.subplots(k, 1, figsize=(10, 2*k), sharex=True)

    for i in range(k):
        # Parameter evolution over MCMC steps
        axes[i].plot(samples_p[:, i], color='black', alpha=0.5)
        axes[i].set_ylabel(f"b{i}")

    axes[-1].set_xlabel("MCMC Step")
    plt.suptitle(f"Trace Plots (Poisson, Degree {degree})")
    plt.tight_layout()
    plt.show()


    # --- Corner plot (posterior distributions + correlations) ---
    labels = [f"b{i}" for i in range(k)]

    fig = corner.corner(
        samples_p,  
        labels=labels,
        quantiles=[0.16, 0.5, 0.84],
        show_titles=True,
        levels=(
            (1 - np.exp(-(1)**2 /2)),
            (1 - np.exp(-(2)**2 /2)),
            (1 - np.exp(-(3)**2 /2))
        )
    )
    plt.suptitle(f"Posterior Distributions (Degree {degree})")
    plt.show()
