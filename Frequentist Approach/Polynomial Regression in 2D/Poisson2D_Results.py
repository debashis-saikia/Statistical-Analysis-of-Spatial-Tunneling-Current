import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from model_metrics_Poisson2d import (plot_fit_2d_poisson, plot_projection_poisson, plot_fit_2d_log, plot_projection_log)
from Poisson_Analysis import PoissonRegression2D

data = pd.read_csv(
    r"C:\Users\IISER13\OneDrive\Desktop\PHY 5032\processed_stm_dataset_1.csv"
)

x = data["x_nm"].values
y = data["y_nm"].values
x = x[:20000]
y = y[:20000]


z = data["log_current"].values
z = z[:20000]

aic_values = []
bic_values = []
chi2_red_values = []
deviance_values = []
deviance_red_values = []

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
