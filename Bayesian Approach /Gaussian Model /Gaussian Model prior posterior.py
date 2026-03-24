# Log-prior
def log_prior_gaussian(theta):
    # Split parameters → beta (coefficients) and sigma (noise)
    beta = theta[:-1]
    sigma = theta[-1]

    # Enforce positive noise (valid probability)
    if sigma <= 0:
        return -np.inf

    # Non-informative prior ~ 1/sigma (scale-invariant)
    return -np.log(sigma)


# Log-posterior
def log_posterior_gaussian(theta, x, y, z, model_func):
    # Extract parameters
    beta = theta[:-1]   # polynomial coefficients
    sigma = theta[-1]   # noise parameter

    # Model prediction
    z_model = model_func(x, y, beta)

    # Posterior = prior + Gaussian log-likelihood
    return (
        log_prior_gaussian(theta)
        -0.5*np.sum(np.log(2*np.pi*sigma**2) + (z - z_model)**2/sigma**2)
    )
