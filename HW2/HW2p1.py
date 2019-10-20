# Template File for Homework 2, Problem 1
# PHYS 331
# Amy Oldenburg
#-------------------------------------
import numpy as np

def calculateSum_16bit(delta):
    sum = np.float16(0.0)
    delta = np.float16(delta)  # Convert delta to a 16-bit floating point number.

    if delta == np.float16(0.0):  # If the 16-bit representation is exactly zero, throw an error.
        print("Error: delta = " + str(delta) + " is equal to zero at this precision of 16 bits.")
        return

    for i in range(0, int(round(1.0 / delta))):  # Compute the sum using a for loop.
        sum += delta
    return sum

def calculateSum_32bit(delta):
    sum = np.float32(0.0)
    delta = np.float32(delta)  # Convert delta to a 32-bit floating point number.

    if delta == np.float32(0.0):  # If the 32-bit representation is exactly zero, throw an error.
        print("Error: delta = " + str(delta) + " is equal to zero at this precision of 32 bits.")
        return

    for i in range(0, int(round(1.0 / delta))):  # Compute the sum using a for loop.
        sum += delta
    return sum

def calculateSum_64bit(delta):
    sum = np.float64(0.0)
    delta = np.float64(delta)  # Convert delta to a 64-bit floating point number.

    if delta == np.float64(0.0):  # If the 64-bit representation is exactly zero, throw an error.
        print("Error: delta = " + str(delta) + " is equal to zero at this precision of 64 bits.")
        return

    for i in range(0, int(round(1.0 / delta))):  # Compute the sum using a for loop.
        sum += delta
    return sum
#--------------------------------
    

print('16 bit, delta 10^-1')
print(calculateSum_16bit(10**-1))
print('\n16 bit, delta 10^-2')
print(calculateSum_16bit(10**-2))
print('\n16 bit, delta 10^-3')
print(calculateSum_16bit(10**-3))
print('\n16 bit, delta 10^-4')
print(calculateSum_16bit(10**-4))
print('\n16 bit, delta 10^-5')
print(calculateSum_16bit(10**-5))



print('\n32 bit, delta 10^-1')
print(calculateSum_32bit(10**-1))
print('\n32 bit, delta 10^-2')
print(calculateSum_32bit(10**-2))
print('\n32 bit, delta 10^-3')
print(calculateSum_32bit(10**-3))
print('\n32 bit, delta 10^-4')
print(calculateSum_32bit(10**-4))
print('\n32 bit, delta 10^-5')
print(calculateSum_32bit(10**-5))

print('\n64 bit, delta 10^-1')
print(calculateSum_64bit(10**-1))
print('\n64 bit, delta 10^-2')
print(calculateSum_64bit(10**-2))
print('\n64 bit, delta 10^-3')
print(calculateSum_64bit(10**-3))
print('\n64 bit, delta 10^-4')
print(calculateSum_64bit(10**-4))
print('\n64 bit, delta 10^-5')
print(calculateSum_64bit(10**-5))
