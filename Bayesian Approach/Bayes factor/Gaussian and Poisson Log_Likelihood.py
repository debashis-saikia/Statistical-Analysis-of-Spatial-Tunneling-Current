def log_likelihood_gaussian(theta, x, y, z, model_func):
    beta = theta[:-1]
    sigma = theta[-1]

    z_model = model_func(x, y, beta)

    return -0.5 * np.sum(
        np.log(2*np.pi*sigma**2) +
        (z - z_model)**2 / sigma**2
    )


def log_likelihood_poisson(beta, x, y, curr, model_func):

    z_model = model_func(x, y, beta)
    z_model = np.clip(z_model, -50, 50)

    lam = np.exp(z_model)
    lam = np.clip(lam, 1e-10, None)

    return np.sum(curr * np.log(lam) - lam)

