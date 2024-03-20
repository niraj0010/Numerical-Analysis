import math

def F(x):
    return 5 * math.exp(x) - 56 * math.sin(x) + 17 * x

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) /(2*h)

def richardsons_extrapolation(f, x, h, k):
    N = [[0] * (k+1) for _ in range(k+1)]
    for i in range(k+1):
        N[i][0] = central_difference(f, x, h / (2 ** i))

    for j in range(1, k+1):
        for i in range(j, k+1):
            N[i][j] = N[i][j-1] + (N[i][j-1] - N[i-1][j-1]) / ((2 ** (2 * j)) - 1)

    return N[k][k]

x0 = 5
h = 0.8
k = 4

result = richardsons_extrapolation(F, x0, h, k)
print(" The derivative of given function using Richardson's Extrapolation :N4(h) =", result)
