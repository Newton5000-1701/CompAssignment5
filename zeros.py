#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:22:22 2024

@author: isaacthompson
"""

import math

# Define the function f(x) = cos(5x) - 2x^2
def f(x):
    return math.tanh(x) - 0.5*x


#BISECTION


a = float(input("For bisection, enter the lower bound: "))  # Lower bound of the interval
b = float(input("For bisection, enter the upper bound: "))  # Upper bound of the interval
tol = float(input("Enter the tolerance: "))  # Tolerance for the solution
dif = a - b

def diff(a, b):
    if dif > 0:
        return None
    
check = diff(a, b)
if check is not None:
        print("Range is unphysical: a must be less than b. Choose a different range.")
        

# Bisection method implementation
def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Bisection method fails for the given range. Choose a different range.")
    
        return None

    # Iteration: this tests on which side of the range the zero is on. If it is on the left of the midpoint, the midpoint is made
    # the new right bound. If the root is on the right of the midpoint the midpoint is made the new left bound. This is repeated
    # until tolerance criteria are met. 
    
    iteration = 0
    
    while (b - a) / 2.0 > tol:
        iteration += 1
        
        midpoint = (a + b) / 2.0
        
        
        if f(midpoint) == 0:
            return midpoint  # This is the case of the exact solution. 
        elif f(a) * f(midpoint) < 0:
            b = midpoint  # The root lies between a and midpoint
        else:
            a = midpoint  # The root lies between midpoint and b
        
        
    return (a + b) / 2.0, iteration

#NEWTON-RAPHSON

def derivative(f, x, h):
    return (f(x + h) - f(x)) / h

# Newton-Raphson implementation
def newton_raphson(a_0, h, tol, max_iter=1000):
    iteration = 0
    A = a_0  # Initial guess
    
    while abs(f(A)) > tol and iteration < max_iter:
        # Calculate derivative using the finite difference method
        der_f = derivative(f, A, h)
        
        if der_f == 0:
            print("Derivative is zero. Stopping to avoid division by zero.")
            return None
        
        # Newton-Raphson update step
        A = A - f(A) / der_f
        
        iteration += 1
        print(f"Newt-Raph Iteration {iteration}: A = {A:.6f}, f(A) = {f(A):.6f}")
    
    if abs(f(A)) <= tol:
        print(f"Converged to root with Newt-Raph at A = {A:.6f} in {iteration} iterations.")
        return A
    else:
        print("Maximum iterations for Newt-Raph reached without convergence.")
        return None


a_0 = float(input("For Newt-Raph, enter initial guess: "))  # Initial guess for the root
h = float(input("For Newt-Raph, enter the step size for the derivative calculation (h): "))




rootNR = newton_raphson(a_0, h, tol)
if rootNR is not None:
    print(f"The root of the equation for Newt-Raph is approximately: {rootNR:.6f}")



rootB, num_iterB = bisection(a, b, tol)
if rootB is not None:
    print(f"The root of the equation for bisection is approximately: {rootB:.6f}")
    print(f"Number of iterations for bisection: {num_iterB}")
