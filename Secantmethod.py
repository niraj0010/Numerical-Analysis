from math import exp, cos

def secant_method_formula(p0, p1, f_p0, f_p1):
    return p1 - f_p1 * (p1 - p0) / (f_p1 - f_p0)

def my_function(x):
    return exp(x) + 5**(-x) - 6 * cos(x) - 5

def secant_method(f, p0, p1, tol=1e-5, max_iter=100):
    iter_count = 0

    while abs(f(p1)) > tol and iter_count < max_iter:
        f_p0, f_p1 = f(p0), f(p1)
        p_next = secant_method_formula(p0, p1, f_p0, f_p1)
        p0, p1, iter_count = p1, p_next, iter_count + 1
        print(f"Iteration {iter_count}: x = {p1}, f(x) = {f(p1)}")

    return p1, iter_count

# Initial guesses
p0, p1 = 0.6, 2.3

# Call the secant method
root_approximation, iterations = secant_method(my_function, p0, p1)

# Print the final result
print(f"\nFinal Approximate root: {root_approximation}")
print(f"Total Iterations: {iterations}")
