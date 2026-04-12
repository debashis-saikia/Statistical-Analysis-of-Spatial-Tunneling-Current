# For Poisson
import matplotlib.pyplot as plt

x_param = samples_p[:, 0]
y_param = samples_p[:, 1]

plt.figure()
plt.hist2d(x_param, y_param, bins=50, cmap='viridis')

plt.xlabel("b0")
plt.ylabel("b1")
plt.title("2D Credible Region")
plt.colorbar(label="Density")
plt.show()
