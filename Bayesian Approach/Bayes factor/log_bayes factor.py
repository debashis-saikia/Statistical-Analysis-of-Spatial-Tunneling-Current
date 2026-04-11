# number of data points
N = len(z)

# marginal likelihoods
logL_g = logsumexp(logL_g_samples) - np.log(len(logL_g_samples))
logL_p = logsumexp(logL_p_samples) - np.log(len(logL_p_samples))

# Bayes factor
log_B = logL_g - logL_p

print("log Bayes Factor:", log_B)
print("Bayes Factor:", B)

# normalize per data point
logL_g_N = logL_g / N
logL_p_N = logL_p / N

log_B_N = logL_g_N - logL_p_N
print("log Bayes Factor (per point):", log_B_N)

# Plot

plt.bar(["Gaussian","Poisson"], [logL_g, logL_p])
plt.ylabel("Average Log-Likelihood")
plt.title("Model Comparison")
plt.show()
