Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:O8:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Gradient Descent for Linear Regression
... import numpy as np
... import matplotlib.pyplot as plt
... 
... # Sample data
... x = np.array([1, 2, 3, 4, 5])
... y = np.array([2, 4, 6, 8, 10])
... 
... # Initialize parameters
... m = 0  # slope
... b = 0  # intercept
... learning_rate = 0.01
... epochs = 1000
... 
... n = len(x)
... 
... # Gradient Descent Algorithm
... for i in range(epochs):
...     y_pred = m * x + b
...     error = y - y_pred
...     cost = (1/n) * sum(error ** 2)
... 
...     # Calculate gradients
...     m_grad = -(2/n) * sum(x * error)
...     b_grad = -(2/n) * sum(error)
... 
...     # Update parameters
...     m = m - learning_rate * m_grad
...     b = b - learning_rate * b_grad
... 
... print(f"Final slope (m): {m}")
... print(f"Final intercept (b): {b}")
... 
... # Plot
... plt.scatter(x, y)
... plt.plot(x, m * x + b, color='red')
... plt.title("Linear Regression using Gradient Descent")
plt.xlabel("x")
plt.ylabel("y")
