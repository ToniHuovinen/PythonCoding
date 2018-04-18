# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 2018

@author: Toni Huovinen
"""

# Hamming encoding and decoding for one bit error

import numpy as np

# Counter for e bit sequence
counter = 0
i = 0

# Base for random error
e = np.array([0,0,0,0,0,0,0])

error_spot = np.random.randint(0, 7)
e[error_spot] = 1

m = np.array([0,0,1,0])


# Generator Matrix, contains Identity Matrix
G = np.array([[1, 0, 0, 0, 1, 0, 1],
              [0, 1, 0, 0, 1, 1, 1],
              [0, 0, 1, 0, 0, 1, 1],
              [0, 0, 0, 1, 1, 1, 0]])


# Parity-check matrix, contains Identity Matrix
H = np.array([[1, 1, 0, 1, 1, 0, 0],
              [0, 1, 1, 1, 0, 1, 0],
              [1, 1, 1, 0, 0, 0, 1]])

# Calculate the codeword
codeword = np.dot(m, G)
codeword = np.mod(codeword, 2)
codeword = codeword.reshape(1,7)

# Add error e to codeword
r = np.add(codeword, e)
r = np.mod(r, 2)
r = r.reshape(7,1)

# Calculate parity-check * r(transpose)

Hrt = np.dot(H, r)
Hrt = np.mod(Hrt, 2)
Hrt = Hrt.reshape(3,1)


# Go through H-chart and compare Hrt to it. Counter goes up every round if there is no equal value.
# When it finds equal, stops
for i in range(len(H[0,:])):
    
    if np.array_equal(H[:,[i]], Hrt):
        counter = counter +1
        break
    else:
        counter = counter +1


# Update e so that counter designated 0 becomes 1
e[error_spot] = 0
e[counter-1] = 1
e = e.reshape(1,7)

# Calculate r + e
r = r.reshape(1,7)
C = np.add(r, e)
C = np.mod(C, 2)

# Print out the decoded codeword
print("Original codeword is: ")
print(m)
print("Encoded word (incl. error):")
print(r)
print("Decoded word:")
print(C[0, 0:4])









