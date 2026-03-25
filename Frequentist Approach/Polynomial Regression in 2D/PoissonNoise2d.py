import numpy as np
from scipy.special import gammaln


def poisson_model_2d(x, y, beta, model_func):
    """
    Generates observations using Poisson noise model for 2D spatial data.

    Parameters
    ----------
    x, y : arrays
        Coordinates
    beta : array
        Model parameters
    model_func : function
        f(x, y, beta) -> expected counts (lambda)

    Returns
    -------
    z : array
        Poisson-distributed observations
    """

    lam = model_func(x, y, beta)

    # Ensure positivity (critical for Poisson)
    lam = np.clip(lam, 1e-10, None)

    z = np.random.poisson(lam)

    return z


def poisson_likelihood_2d(x, y, z, beta, model_func):
    """
    Computes likelihood for Poisson noise model.
    """

    lam = model_func(x, y, beta)
    lam = np.clip(lam, 1e-10, None)

    likelihood = np.prod(
        (lam**z * np.exp(-lam)) / np.exp(gammaln(z + 1))
    )

    return likelihood


def log_poisson_likelihood_2d(x, y, z, beta, model_func):
    """
    Computes log-likelihood for Poisson model.
    """

    lam = model_func(x, y, beta)
    lam = np.clip(lam, 1e-10, None)

    logL = np.sum(
        z * np.log(lam) - lam - gammaln(z + 1)
    )

    return logL


def poisson_deviance_2d(x, y, z, beta, model_func):
    """
    Poisson deviance (analog of RSS for Poisson).
    """

    lam = model_func(x, y, beta)
    lam = np.clip(lam, 1e-10, None)

    term = np.where(
        z > 0,
        z * np.log(z / lam) - (z - lam),
        -lam
    )

    D = 2 * np.sum(term)

    return D


def pearson_chi_square_2d(x, y, z, beta, model_func):
    """
    Pearson chi-square for Poisson model.
    """

    lam = model_func(x, y, beta)
    lam = np.clip(lam, 1e-10, None)

    chi2 = np.sum((z - lam)**2 / lam)

    return chi2


def degrees_of_freedom(N, p):
    return N - (p + 1)


def reduced_poisson_deviance_2d(x, y, z, beta, model_func, p):
    """
    Reduced deviance (Poisson analog of reduced chi-square)
    """

    D = poisson_deviance_2d(x, y, z, beta, model_func)

    nu = degrees_of_freedom(len(z), p)

    return D / nu