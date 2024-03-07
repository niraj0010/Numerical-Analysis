import matplotlib.pyplot as plt

def divided_difference(x, y):
    n = len(x)
    F = [[0] * n for _ in range(n)]
    
    for i in range(n):
        F[i][0] = y[i]
    
    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i])
    
    return [F[0][j] for j in range(n)]

def interpolating_polynomial(x, coefficients, input_x):
    result = coefficients[0]  # Start with the constant term
    for i, coef in enumerate(coefficients[1:]):  # Skip the constant term
        term = coef
        for j in range(i + 1):
            term *= (input_x - x[j])
        result += term
    return result

# Given datas
x_data = [2.9, 3.7, 4.9, 5.1, 6.8]
y_data = [146, 186, 381, 442, 1390]

coefficients = divided_difference(x_data, y_data)

degree = min(len(x_data) - 1, 4)
print("Interpolating Polynomial Coefficients :")
for i, coef in enumerate(coefficients[:degree + 1]):
    print(f"a{i} = {coef}")

x_interpolated = [min(x_data) + i * 0.1 for i in range(int((max(x_data) - min(x_data)) / 0.1) + 1)]
y_interpolated = [interpolating_polynomial(x_data, coefficients, x) for x in x_interpolated]

# Plotting
plt.scatter(x_data, y_data, label='Data Points')
plt.plot(x_interpolated, y_interpolated, label='Interpolating Polynomial', color='purple')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graph: Interpolating Polynomial and the given data')
plt.legend()
plt.show()
