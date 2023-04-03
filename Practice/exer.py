from scipy.misc import derivative

def func(x):
    return x**3 + 2*x**2 + x

Res= derivative(func, 2, dx=1e-6)

print(Res)

