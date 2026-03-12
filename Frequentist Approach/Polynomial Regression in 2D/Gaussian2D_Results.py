import numpy as np
import matplotlib.pyplot as plt
from model_metrics2d import (plot_fit_2d, plot_projection)
from Gaussian_Analysis2d import PolynomialRegression2D
import pandas as pd

data = pd.read_csv(r"C:\Users\IISER13\OneDrive\Desktop\PHY 5032\processed_stm_dataset_1.csv")

x = data["x_nm"].values
y = data["y_nm"].values
z = data["log_current"].values

#model = PolynomialRegression2D(degree=2)
#model.fit(x, y, z)
#model.model_info()
#z_pred = model.predict(x, y)

#plot_fit_2d(x, y, z, model.polynomial_model, model.beta_hat, model.degree)
#plot_projection(x, y, z, model.polynomial_model, model.beta_hat, model.degree)

aic_values = []
bic_values = []
chi2_red_values = [] 
for degree in range(1, 5):
    model = PolynomialRegression2D(degree=degree)
    model.fit(x, y, z)
    model.model_info()
    z_pred = model.predict(x, y)
    aic_values.append(model.AIC)
    bic_values.append(model.BIC)
    chi2_red_values.append(model.chi2_red)

for i in range(4):
    print(f"Degree {i+1}: AIC = {aic_values[i]:.2f}, BIC = {bic_values[i]:.2f}, Reduced Chi-Square = {chi2_red_values[i]:.2f}")

plt.plot(range(1, 5), aic_values, marker='o', label='AIC')
plt.plot(range(1, 5), bic_values, marker='s', label='BIC')
plt.xlabel('Degree')
plt.ylabel('Information Criterion')
plt.title('Model Selection')
plt.legend()
plt.show()

plt.plot(range(1, 5), chi2_red_values, marker='o', label='Reduced Chi-Square')
plt.xlabel('Degree')
plt.ylabel('Reduced Chi-Square')
plt.title('Model Fit Quality')
plt.legend()
plt.show()
