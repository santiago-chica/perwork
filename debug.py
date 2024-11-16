from sympy import symbols, solve, sqrt, Eq
from sympy.abc import x, y

this = Eq(-2 * x, 3)
print(this._repr_latex_())
print(solve(this, x))