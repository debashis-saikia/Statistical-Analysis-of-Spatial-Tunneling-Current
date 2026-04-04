def compute_credible_intervals(samples, labels=None):
    """
    Compute 16%, 50%, 84% credible intervals (≈ 1σ)
    """

    percentiles = [16, 50, 84]
    results = np.percentile(samples, percentiles, axis=0)

    lower = results[0]
    median = results[1]
    upper = results[2]

    for i in range(samples.shape[1]):
        name = labels[i] if labels is not None else f"param_{i}"

        print(f"{name}: {median[i]:.4f} (+{upper[i]-median[i]:.4f}, -{median[i]-lower[i]:.4f})")



print("samples_g shape:", samples_g.shape)
print("labels_g length:", len(labels_g))



# Gaussian
k = samples_g.shape[1] - 1   # last is sigma
labels_g = [f"b{i}" for i in range(k)] + ["sigma"]

compute_credible_intervals(samples_g, labels_g)
