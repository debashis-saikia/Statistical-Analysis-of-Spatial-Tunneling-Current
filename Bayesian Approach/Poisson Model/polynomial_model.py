def polynomial_model(self, x, y, beta):

    z_pred = np.zeros_like(x)

    idx = 0
    for i in range(self.degree + 1):
        for j in range(self.degree + 1 - i):
            term = beta[idx] * (x**i) * (y**j)

            # Prevent explosion
            term = np.clip(term, -1e3, 1e3)

            z_pred += term
            idx += 1

    # Final clipping
    z_pred = np.clip(z_pred, -50, 50)

    return z_pred
