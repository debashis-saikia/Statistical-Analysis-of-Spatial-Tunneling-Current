# Bayes factor 
log_B = logL_g - logL_p
B = np.exp(log_B)

print("log Bayes Factor:", log_B)
print("Bayes Factor:", B)

# Plot

plt.bar(["Gaussian","Poisson"], [logL_g, logL_p])
plt.ylabel("Average Log-Likelihood")
plt.title("Model Comparison")
plt.show()
