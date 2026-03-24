# --- MCMC Sampling ---
import emcee
import matplotlib.pyplot as plt
import corner
import numpy as np


def run_mcmc_gaussian(x, y, z, model_func, degree, initial_beta=None):

    import emcee
    import numpy as np

    k = (degree + 1)*(degree + 2)//2
    ndim = k + 1
    nwalkers = 50
    nsteps = 2000
    nburn = 1000

    # --- Initialize walkers ---
    if initial_beta is not None:
        pos = np.zeros((nwalkers, ndim))
        pos[:, :k] = initial_beta + 1e-4*np.random.randn(nwalkers, k)
        pos[:, k] = 0.5 + 1e-4*np.random.randn(nwalkers)
    else:
        pos = np.random.randn(nwalkers, ndim) * 1e-3

    # --- Sampler ---
    sampler = emcee.EnsembleSampler(
        nwalkers, ndim, log_posterior_gaussian,
        args=(x, y, z, model_func)
    )

    sampler.run_mcmc(pos, nsteps, progress=True)

    # --- Get chain ---
    chain = sampler.get_chain()   # shape: (nsteps, nwalkers, ndim)

    # --- Remove burn-in ---
    samples = chain[nburn:, :, :]

    # --- Flatten ---
    samples = samples.reshape(-1, ndim)

    return samples
