# Bayesian Hypothesis Testing in Model Analysis

## Overview

Bayesian hypothesis testing evaluates the statistical significance and reliability of model parameters using **posterior distributions**, **credible intervals**, and **MCMC diagnostics**. This approach provides a probabilistic framework to assess:

- Parameter significance  
- Model stability  
- Overfitting behavior  
- Model complexity  

In this analysis, we compare **polynomial models of different degrees** under **Gaussian noise** and **Poisson noise** assumptions.

---

# Methodology

For each polynomial degree and noise model, we examine:

## 1. Posterior Scatter Plots

- Show correlations between parameters  
- Tight clusters → stable parameters  
- Multiple clusters → degeneracy or overfitting  

## 2. Trace Plots

- Show MCMC convergence behavior  
- Random stationary chains → good convergence  
- Drift or trends → poor convergence  

## 3. Posterior Distribution (Corner Plots)

- Show parameter uncertainty  
- Gaussian distributions → well-constrained parameters  
- Multi-modal distributions → unstable model  

---

# Results: Gaussian Noise Model

## Degree 1

### Scatter Plot

- Tight and compact posterior cloud  
- Nearly circular distribution  
- Minimal parameter correlations  

**Interpretation**  
The parameters are well constrained and stable.

### Posterior Distribution

- Gaussian-shaped distributions  
- Narrow credible intervals  
- No multi-modal structure  

**Interpretation**  
Degree 1 model provides stable parameter estimation.

### Conclusion (Gaussian Degree 1)

- Stable model  
- Minimal uncertainty  
- No overfitting  

**Degree 1 is strongly supported**

---

## Degree 2

### Scatter Plot

- Slightly wider spread  
- Minor parameter correlations  

### Posterior Distribution

- Slightly broader distributions  
- Small correlations appear  

**Interpretation**  
The model becomes slightly more complex without significant improvement.

### Conclusion (Gaussian Degree 2)

- Acceptable model  
- Slight increase in uncertainty  
- Possible beginning of overfitting  

---

## Degree 3

### Scatter Plot

- Larger spread  
- Increased parameter degeneracy  

### Posterior Distribution

- Wider posterior distributions  
- Strong parameter correlations  

**Interpretation**  
Higher-degree model introduces unnecessary parameters.

### Conclusion (Gaussian Degree 3)

- Overfitting behavior observed  
- Increased uncertainty  
- Model becomes less reliable  

---

# Gaussian Model Summary

| Degree | Stability | Complexity | Conclusion |
|--------|-----------|------------|------------|
| Degree 1 | High | Low | Best |
| Degree 2 | Moderate | Moderate | Acceptable |
| Degree 3 | Low | High | Overfitting |

---

# Results: Poisson Noise Model

## Degree 1

### Scatter Plot

- Tight and compact distribution  
- No multi-modal behavior  

### Trace Plot

- Stable chains  
- Good mixing  
- No drift  

### Posterior Distribution

- Gaussian-like distributions  
- Narrow credible intervals  

### Conclusion (Poisson Degree 1)

- Well-constrained parameters  
- Good convergence  
- Stable model  

**Degree 1 is strongly supported**

---

## Degree 2

### Scatter Plot

- Slightly broader distributions  
- Minor correlations  

### Trace Plot

- Stable chains  
- Good convergence  

### Posterior Distribution

- Slightly wider credible intervals  

### Conclusion (Poisson Degree 2)

- Acceptable model  
- Slight increase in uncertainty  
- No strong improvement  

---

## Degree 3

### Scatter Plot

- Multiple clusters  
- Multi-modal structure  

### Trace Plot

- Strong drift  
- Poor mixing  
- Non-stationary chains  

### Posterior Distribution

- Multi-modal distributions  
- Strong parameter correlations  

### Conclusion (Poisson Degree 3)

- Overfitting  
- Poor convergence  
- Unstable parameters  

**Degree 3 is rejected**

---

# Poisson Model Summary

| Degree | Stability | Convergence | Conclusion |
|--------|-----------|-------------|------------|
| Degree 1 | High | Good | Best |
| Degree 2 | Moderate | Good | Acceptable |
| Degree 3 | Low | Poor | Rejected |

---

# Bayesian Model Comparison Using Bayes Factor

To compare Gaussian and Poisson noise models, we computed the Bayes factor using marginal likelihoods estimated from posterior samples.

## Bayes Factor Results

- **Log Bayes Factor** = 2.8  
- **Bayes Factor** = 16.4  

---

## Interpretation

According to the **Jeffreys scale**:

| Log Bayes Factor | Evidence Strength |
|------------------|-------------------|
| < 1 | Weak |
| 1 – 3 | Moderate |
| 3 – 5 | Strong |
| > 5 | Very Strong |

The obtained **log Bayes factor of 2.8** indicates **moderate to strong evidence** in favor of the preferred model.

The Bayes factor of **16.4** implies:

> The preferred model is approximately **16 times more probable** than the competing model given the data.

---

# Gaussian vs Poisson Comparison

Key Observations:

- Both Gaussian and Poisson models favor **lower-degree polynomials**
- Higher-degree models introduce **parameter degeneracy**
- Degree 3 models show **overfitting behavior**
- Degree 1 models show **stable parameter estimation**
- Bayes factor supports the preferred noise model

---

# Final Model Selection

Based on:

- Posterior scatter plots  
- Trace plots  
- Posterior distributions  
- Bayesian hypothesis testing  
- Bayes factor comparison  

## Final Model

- **Polynomial Degree:** 1  
- **Noise Model:** Preferred model from Bayes factor  
- **Model Complexity:** Minimal  
- **Model Stability:** High  

---

# Conclusion

Bayesian hypothesis testing shows that:

- Lower-degree models provide stable parameter estimates  
- Higher-degree models introduce overfitting  
- MCMC diagnostics confirm model reliability  
- Posterior distributions support simpler models  
- Bayes factor provides moderate-to-strong model preference  

---

# Takeaway

Bayesian analysis helps:

- Identify statistically meaningful parameters  
- Detect overfitting  
- Compare models robustly  
- Select physically meaningful models  

---

# Final Recommendation

**Degree 1 polynomial model with the preferred noise model provides the most reliable and interpretable description of the spatial tunneling current data.**
