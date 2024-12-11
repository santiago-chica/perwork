from sympy import symbols, solve, sqrt, Eq
from sympy.abc import x, y

this = Eq(-2 * x, 3)
print(solve(this, x)[0])