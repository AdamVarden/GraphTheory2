#! /usr/bin/env python3

# Adam Varden
# Calculate the square root of a number

def sqrt(x):
  """
  Calculate the square root of argument x
  """
  # lets check that x is positive
  if x < 0:
    print("Error: negative value was supplied")
    return -1


  # Initial guess for the square root  
  z = x / 2.0 
  
  # Continuously improve the guess.
  while abs(x - (z*z)) > 0.01:     
    z = z - (((z*z) - x) / (2*z))
  
  return z

myval = 63.0
print("the square root of",myval,"is", sqrt(63.0))


