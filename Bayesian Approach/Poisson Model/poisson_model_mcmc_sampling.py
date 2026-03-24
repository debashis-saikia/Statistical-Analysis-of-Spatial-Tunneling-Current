# MCMC

import emcee
import numpy as np

def run_mcmc_poisson(x, y, curr, model_func, degree, initial_beta=None):

    # Number of polynomial parameters
    k = (degree + 1)*(degree + 2)//2

    ndim = k           # parameters = only beta
    nwalkers = 60      # number of MCMC walkers
    nsteps = 3000      # total steps
    nburn = 2000       # burn-in steps

    # --- Initialize walkers ---
    if initial_beta is not None:
        # Start near frequentist solution (stable initialization)
        pos = initial_beta + 1e-2 * np.random.randn(nwalkers, ndim)
    else:
        # Small random initialization
        pos = np.random.randn(nwalkers, ndim) * 1e-3

    # --- Create sampler ---
    sampler = emcee.EnsembleSampler(
        nwalkers, ndim, log_posterior_poisson,
        args=(x, y, curr, model_func)
    )

    # Run MCMC (sample posterior)
    sampler.run_mcmc(pos, nsteps, progress=True)

    # Extract chain → shape (steps, walkers, ndim)
    chain = sampler.get_chain()

    # Remove burn-in (keep converged samples)
    samples = chain[nburn:, :, :]

    # Flatten → (n_samples, ndim)
    samples = samples.reshape(-1, ndim)

    # Thin the samples
    samples = samples[::5]   # take every 5th sample

    return samples
