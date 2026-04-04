def hpd_interval(samples, alpha=0.68):
    """
    Compute Highest Posterior Density interval
    """

    sorted_samples = np.sort(samples)
    n = len(samples)
    interval_idx = int(alpha * n)

    widths = sorted_samples[interval_idx:] - sorted_samples[:n - interval_idx]
    min_idx = np.argmin(widths)

    return sorted_samples[min_idx], sorted_samples[min_idx + interval_idx]




# Use for Gaussian
low, high = hpd_interval(samples_g[:, 0])
print("HPD interval:", low, high)
