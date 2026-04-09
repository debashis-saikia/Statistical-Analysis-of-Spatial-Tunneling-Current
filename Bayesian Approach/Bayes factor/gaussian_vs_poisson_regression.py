from scipy.special import logsumexp

degree = 2

# Convert to counts
curr = np.exp(z)
counts = np.round(100 * curr / np.mean(curr)).astype(int)
counts[counts < 0] = 0
curr_counts = counts

# Gaussian likelihoods
logL_g_samples = np.array([
    log_likelihood_gaussian(
        s, x, y, z, model_g.polynomial_model
    )
    for s in samples_g[:1000]
])

# Poisson likelihoods
logL_p_samples = np.array([
    log_likelihood_poisson(
        s, x, y, curr_counts, model_p.polynomial_model
    )
    for s in samples_p[:1000]
])

# Marginal likelihoods
logL_g = logsumexp(logL_g_samples) - np.log(len(logL_g_samples))
logL_p = logsumexp(logL_p_samples) - np.log(len(logL_p_samples))


print("Gaussian sample length:", len(samples_g[0]))
print("Poisson sample length:", len(samples_p[0]))
