def compute_ess(samples):
    """
    Rough ESS estimate using variance reduction
    """

    N = len(samples)

    # autocorrelation estimate
    var = np.var(samples)
    mean = np.mean(samples)

    autocorr = np.correlate(samples - mean, samples - mean, mode='full')
    autocorr = autocorr[autocorr.size // 2:]
    autocorr /= autocorr[0]

    # find where autocorrelation drops
    cutoff = np.where(autocorr < 0.1)[0]
    tau = cutoff[0] if len(cutoff) > 0 else len(autocorr)

    ess = N / (2 * tau)

    return ess




print("\n--- Effective Sample Size (ESS) ---")

for i in range(samples_p.shape[1]):
    ess = compute_ess(samples_p[:, i])
    print(f"Parameter b{i}: ESS ≈ {ess:.1f}")
