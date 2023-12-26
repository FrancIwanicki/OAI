import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

m = 100
X = np.linspace(-3, 3, m)
y = 2 * np.sin(X) + np.random.uniform(-0.5, 0.5, m)

fig, ax = plt.subplots()
ax.scatter(X, y, edgecolors=(0, 0, 0))
plt.show()
poly_features = PolynomialFeatures(degree=3, include_bias=False)
X_poly = poly_features.fit_transform(X)
print("X[0] = ",X[0])
print("X[1] = ",X[1])
print("Y[1] = ",y[1])
lin_reg = linear_model.LinearRegression()
lin_reg.fit(X_poly, y)
print("Перетин:",lin_reg.intercept_,"Коефіцієнти регресії", lin_reg.coef_)
y_pred = lin_reg.predict(X_poly)

print("X_poly = ",X_poly)


fig, ax = plt.subplots()
ax.scatter(X, y, edgecolors=(0, 0, 0))
plt.plot(X, y_pred, color='red', linewidth=4)
plt.show()
