import numpy as np
import matplotlib.pyplot as plt
import math

def taylor_sin(x, n_terms):
    sin_x = 0
    for n in range(n_terms):
        # Derivatives of sin(x) at 0: 
        # 0th derivative = sin(0) = 0, 
        # 1st derivative = cos(0) = 1, 
        # 2nd derivative = -sin(0) = 0,
        # 3rd derivative = -cos(0) = -1, ...
        if n % 2 == 0:
            derivative_at_zero = 0  # even derivatives are 0
        else:
            derivative_at_zero = (-1)**((n - 1) // 2)  # odd derivatives alternate between 1 and -1
        
        term = derivative_at_zero * (x**n) / math.factorial(n)
        sin_x += term
    return sin_x


x_value = 2
n_terms = 15
sin_2 = taylor_sin(x_value, n_terms)
print(f"Taylor series approximation of sin(2) with {n_terms} terms: {sin_2}")

x_range = np.arange(-10, 10.1, 0.1)
taylor_approx = [taylor_sin(x, n_terms) for x in x_range]

true_sin = np.sin(x_range)

plt.figure(figsize=(10, 6))
plt.plot(x_range, taylor_approx, label=f'Taylor Series (n={n_terms})', color='blue', linestyle='--')
plt.plot(x_range, true_sin, label='sin(x) (True)', color='red')
plt.title('Taylor Series Approximation of sin(x) (n=15)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.legend()

plt.ylim(-2, 2)

plt.savefig('taylor_n15.png')
plt.show()

plt.figure(figsize=(10, 6))
for n in range(1, n_terms + 1):
    taylor_approx_n = [taylor_sin(x, n) for x in x_range]
    plt.plot(x_range, taylor_approx_n, label=f'n={n}')

plt.plot(x_range, true_sin, label='sin(x) (True)', color='red', linewidth=2)
plt.title('Successive Approximations of sin(x) (n=1 to n=15)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.legend(loc='lower left')

plt.ylim(-2, 2)

plt.savefig('taylor_successive.png')
plt.show()





        