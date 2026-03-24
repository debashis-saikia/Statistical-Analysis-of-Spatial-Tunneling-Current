for degree in range(1, 5):

    print(f"\n--- Running MCMC for Degree {degree} ---")

    # --- Fit frequentist model (good initial guess) ---
    model = PolynomialRegression2D(degree=degree)
    model.fit(x, y, z)

    # --- Run MCMC ---
    samples_g = run_mcmc_gaussian(
        x, y, z,
        model.polynomial_model,
        degree,
        initial_beta=model.beta_hat
    )

    # samples shape: (n_samples, ndim)
    print("Samples shape:", samples_g.shape)


    # --- Scatter plot (first two parameters) ---
    plt.figure()
    plt.plot(samples_g[:, 0], samples_g[:, 1], 'k.', alpha=0.1)
    plt.title(f"Posterior Scatter (Degree {degree})")
    plt.xlabel("b0")
    plt.ylabel("b1")
    plt.show()


    # --- Corner Plot ---
    k = (degree + 1)*(degree + 2)//2
    labels = [f"b{i}" for i in range(k)] + ["sigma"]

    fig = corner.corner(
        samples_g,   
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
