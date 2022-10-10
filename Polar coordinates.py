#You are given a complex . Your task is to convert it to polar coordinates.

#Input Format
#A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.

#Constraints
#Given number is a valid complex number

#Output Format
#Output two lines:
#The first line should contain the value of modulus r.
#The second line should contain the value of phase angle ph.

#Code
import cmath

z=complex(input())
print(abs(z))
print(cmath.phase(z))
