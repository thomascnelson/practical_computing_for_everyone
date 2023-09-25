# create some fake data
import numpy as np
concentration = np.array([1,2,4,8,16])
absorbance = np.array([1.8,4.7,7.7,19.1,37.1])

# plot it
import matplotlib.pyplot as plt
plt.scatter(concentration, absorbance)
plt.title("Standard Curve")
plt.xlabel("Input Concentration")
plt.ylabel("Output Absorbance")
plt.savefig('my_figure1.png', dpi=500)
plt.show()

# explore it
print(concentration.shape)
print(absorbance.shape)

# use scikit-learn linear regression module
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(absorbance.reshape(-1, 1), concentration)

# look at coefficient and intercept of the line
print(regressor.coef_)
print(regressor.intercept_)

# generate predict values manually to plot line
predicted_conc = regressor.coef_ * absorbance + regressor.intercept_

# plot the line on top of the data
plt.scatter(absorbance, concentration)
plt.plot(absorbance, predicted_conc)
plt.title("Standard Curve")
plt.ylabel("Concentration")
plt.xlabel("Absorbance")
plt.savefig('my_figure2.png', dpi=500)
plt.show()

# look at model performance by the coefficient of determination
from sklearn.metrics import r2_score
r2_score(concentration, predicted_conc)

# predict unknowns with predict function
unknown_abs = 13.5
regressor.predict(np.array(unknown_abs).reshape(1, -1))

# predict unknowns manually
unknown_abs = 13.5
unknown_conc = regressor.coef_ * unknown_abs + regressor.intercept_
unknown_conc

