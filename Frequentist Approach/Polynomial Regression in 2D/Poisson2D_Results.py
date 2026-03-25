import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from model_metrics2d import (plot_fit_2d_poisson, plot_projection_poisson, plot_fit_2d_log, plot_projection_log)
from Poisson_Analysis import PoissonRegression2D

data = pd.read_csv(
    r"C:\Users\IISER13\OneDrive\Desktop\PHY 5032\processed_stm_dataset_1.csv"
)

x = data["x_nm"].values
y = data["y_nm"].values
x = x[:20000]
y = y[:20000]

#x = (x - np.mean(x)) / np.std(x)
#y = (y - np.mean(y)) / np.std(y)

z = data["log_current"].values
z = z[:20000]
z = np.abs(z)  # ensure non-negativity

#current = np.exp(log_current)

#current = current / np.mean(current)

#z = np.round(current * 50).astype(int)   # scale factor tunable

#z = np.clip(current, 1, None)


aic_values = []
bic_values = []
chi2_red_values = []
deviance_values = []
deviance_red_values = []


'''for degree in range(1, 5):

    print(f"\n========== Degree {degree} ==========")

    model = PoissonRegression2D(degree=degree)
    model.fit(x, y, z)

    model.model_info()

    aic_values.append(model.AIC)
    bic_values.append(model.BIC)
    chi2_red_values.append(model.chi2_red)
    deviance_values.append(model.deviance)
    deviance_red_values.append(model.deviance_red)'''


'''print("\n===== Model Comparison =====")

for i in range(4):

    print(
        f"Degree {i+1}: "
        f"AIC = {aic_values[i]:.2f}, "
        f"BIC = {bic_values[i]:.2f}, "
        f"Chi2_red = {chi2_red_values[i]:.2f}, "
        f"Dev = {deviance_values[i]:.2f}, "
        f"Dev_red = {deviance_red_values[i]:.2f}"
    )

plt.figure()
plt.plot(range(1, 5), aic_values, marker='o', label='AIC')
plt.plot(range(1, 5), bic_values, marker='s', label='BIC')
plt.xlabel('Polynomial Degree')
plt.ylabel('Information Criterion')
plt.title('Poisson Model Selection')
plt.legend()
plt.grid()
plt.show()
plt.figure()
plt.plot(range(1, 5), chi2_red_values, marker='o')
plt.axhline(1, linestyle='--')  # ideal value
plt.xlabel('Polynomial Degree')
plt.ylabel('Reduced Chi-Square')
plt.title('Poisson Fit Diagnostic')
plt.grid()
plt.show()
plt.figure()
plt.plot(range(1, 5), deviance_red_values, marker='o')
plt.axhline(1, linestyle='--')
plt.xlabel('Polynomial Degree')
plt.ylabel('Reduced Deviance')
plt.title('Primary Goodness-of-Fit (Poisson)')
plt.grid()
plt.show()
plt.figure()
plt.plot(range(1, 5), deviance_values, marker='o')
plt.xlabel('Polynomial Degree')
plt.ylabel('Poisson Deviance')
plt.title('Model Deviance')
plt.grid()
plt.show()'''

for i in range(1, 7):
    degree=i
    model = PoissonRegression2D(degree)

    model.fit(x, y, z)

    model.summary()

    z_pred = model.predict(x, y)

    aic_values.append(model.AIC)
    bic_values.append(model.BIC)
    plot_fit_2d_poisson(x, y, z, model)

    plot_projection_poisson(x, y, z, model)

plt.figure()
plt.plot(range(1, 7), aic_values, marker='o', label='AIC')
plt.plot(range(1, 7), bic_values, marker='s', label='BIC')
plt.xlabel('Polynomial Degree')
plt.ylabel('Information Criterion')
plt.title('Poisson Model Selection')
plt.legend()
plt.grid()
plt.show()


#plot_fit_2d_log(x, y, z, model)
#plot_projection_log(x, y, z, model)