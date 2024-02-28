import cmath

def g(x):
    return 100*x**5 - 50*x**4 + 30*x**3 - 1000

# Initial guesses provided:
initial_p0 = 1
initial_p1 = 1.5
initial_p2 = 2

def muller_method(p0, p1, p2, tol=1e-5, max_iteration=100):
    iteration = 1

    while iteration <= max_iteration:
        c = g(p2)
        numerator1 = (p0 - p2)**2 * (g(p1) - g(p2))
        numerator2 = (p1 - p2)**2 * (g(p0) - g(p2))
        denominator = (p0 - p2) * (p1 - p2) * (p0 - p1)
        b = (numerator1 - numerator2) / denominator

        numerator1 = (p1 - p2) * (g(p0) - g(p2))
        numerator2 = (p0 - p2) * (g(p1) - g(p2))
        a = (numerator1 - numerator2) / denominator

        h = -2 * c / (b + cmath.sqrt(b**2 - 4 * a * c))
        p = p2 + h

        print(f"Iteration {iteration}: Approximate root = {p.real}")

        if abs(h) < tol:
            return p.real

        p0, p1, p2 = p1, p2, p
        iteration += 1

    print(" The maximum number of iterations has been reached.")
    return None


root = muller_method(initial_p0, initial_p1, initial_p2)
if root:
    print("Approximate root:", root)
