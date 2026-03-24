degree = 2

#Gaussian
model_g = PolynomialRegression2D(degree=degree)
model_g.fit(x, y, z)

logL_g = np.mean([
    log_likelihood_gaussian(s, x, y, z, model_g.polynomial_model)
    for s in samples_g[:1000]
])

# Poisson

model_p = PolynomialRegression2D(degree=degree)

curr = np.exp(z)

logL_p = np.mean([
    log_likelihood_poisson(s, x, y, curr, model_p.polynomial_model)
    for s in samples_p[:1000]
])


print("Gaussian sample length:", len(samples_g[0]))
print("Poisson sample length:", len(samples_p[0]))
