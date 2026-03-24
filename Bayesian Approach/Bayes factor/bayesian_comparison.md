# Bayesian Model Comparison: Gaussian vs Poisson

---

## Bayesian Gaussian Model

The Gaussian model assumes that the noise in the data follows a normal distribution with constant variance. Using MCMC sampling, the posterior distributions of the polynomial coefficients and noise parameter ($\sigma$) were obtained.

The model provides a good fit to the **log-transformed current**, and the posterior distributions show well-behaved parameter estimates with reasonable uncertainty.

However, the Gaussian assumption implies **constant variance**, which may not accurately reflect the statistical nature of STM data.

---

## Bayesian Poisson Model

The Poisson model directly describes the **count-based nature of the current**, where the variance is equal to the mean. In this case, the polynomial model is used to describe the log of the rate parameter ($\lambda$), and MCMC sampling is used to estimate the posterior distributions of the coefficients.

Unlike the Gaussian model, the Poisson model does not require an explicit noise parameter, as the noise is inherently determined by the signal.

This makes the Poisson model **physically more appropriate** for STM data, where fluctuations arise from discrete tunneling events.

---

## Bayes Factor Comparison

The model comparison was performed using the Bayes factor, computed from the average log-likelihood over posterior samples.

* **Log Bayes Factor**:

$$
\log B = -251358
$$

* **Bayes Factor**:

$$
B \approx 0
$$

Due to numerical underflow, the Bayes factor evaluates to zero. However, the extremely large negative value of the log Bayes factor indicates **overwhelming evidence in favor of the Poisson model**.

---

## Interpretation (Jeffreys Scale)

According to Jeffreys’ scale:

* $|\log B| \gg 10$ indicates **decisive evidence**

In this case:

* $\log B = -251358$ → **extremely strong evidence for the Poisson model**

---

## Final Conclusion

> The Bayesian analysis strongly favors the **Poisson model** over the Gaussian model.
>
> While the Gaussian model provides a reasonable fit to the log-transformed data, it assumes constant variance and does not capture the underlying count-based noise structure.
>
> In contrast, the Poisson model directly incorporates the signal-dependent variance inherent in STM measurements, leading to a more physically meaningful and statistically consistent description of the data.
>
> The extremely large magnitude of the log Bayes factor confirms that the Poisson model provides a **decisively better explanation** of the observed data.

---

## One-line Conclusion

> *“The Bayesian comparison shows overwhelming evidence in favor of the Poisson model, as it correctly captures the count-based noise structure of STM data.”*
