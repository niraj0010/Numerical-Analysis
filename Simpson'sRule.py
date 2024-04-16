def f(x):
    return (9 * x**2 - 2) / (x + 5)

def simpsons_rule(a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    fx = [f(x_i) for x_i in x]

    result = fx[0] + fx[-1]  # First and last terms

    result += sum(4 * fx[i] for i in range(1, n, 2))

    # Terms with odd index
    result += sum(2 * fx[i] for i in range(2, n-1, 2))

    result *= h / 3

    return result

a = -3
b = 5

# Number of subintervals
n = 50

approximation = simpsons_rule(a, b, n)
print("Approximation of the integral:", approximation)
