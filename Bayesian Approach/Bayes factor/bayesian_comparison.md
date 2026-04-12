# Bayesian Model Comparison: Gaussian vs Poisson

---

## Bayesian Gaussian Model

The Gaussian model assumes that the noise in the data follows a normal distribution with constant variance. Using MCMC sampling, the posterior distributions of the polynomial coefficients and noise parameter ($\sigma$) were obtained.

The model provides a good fit to the **log-transformed current**, and the posterior distributions show well-behaved parameter estimates with reasonable uncertainty.

The Gaussian assumption of **constant variance** is suitable when the transformed data exhibits approximately uniform fluctuations, making the Gaussian model statistically consistent for the analyzed dataset.

---

## Bayesian Poisson Model

The Poisson model directly describes the **count-based nature of the current**, where the variance is equal to the mean. In this case, the polynomial model is used to describe the log of the rate parameter ($\lambda$), and MCMC sampling is used to estimate the posterior distributions of the coefficients.

Unlike the Gaussian model, the Poisson model does not require an explicit noise parameter, as the noise is inherently determined by the signal.

However, for the present dataset, the Poisson model shows **larger uncertainty**, poorer convergence for higher polynomial degrees, and less stable posterior distributions compared to the Gaussian model.

---

## Bayes Factor Comparison

The model comparison was performed using the Bayes factor, computed from the marginal likelihood estimated using posterior samples.

* **Log Bayes Factor**:

$$
\log B = 2.8
$$

* **Bayes Factor**:

$$
B = 16.4
$$

This indicates that the **Gaussian model is preferred over the Poisson model**.

---

## Interpretation (Jeffreys Scale)

According to Jeffreys’ scale:

* $|\log B| > 1$ → Substantial evidence  
* $|\log B| > 2.5$ → Strong evidence  
* $|\log B| > 5$ → Decisive evidence  

In this case:

* $\log B = 2.8$ → **Strong evidence for the Gaussian model**

Thus, the Gaussian model is **statistically favored** over the Poisson model.

---

## Final Conclusion

> The Bayesian analysis favors the **Gaussian model** over the Poisson model.
>
> The Gaussian model provides stable posterior distributions, well-behaved parameter estimates, and better convergence properties.
>
> Although the Poisson model is physically motivated for count-based data, the Bayesian evidence suggests that the Gaussian model provides a **better statistical description** of the observed dataset.
>
> The positive log Bayes factor confirms that the Gaussian model provides a **stronger explanation** of the observed data.

---

## One-line Conclusion

> *“The Bayesian comparison shows strong evidence in favor of the Gaussian model, indicating that Gaussian noise provides a better statistical description of the spatial tunneling current data.”*
