# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 2018

@author: Toni Huovinen
"""

# Code for Linear encoding and decoding, fixing one bit error

import numpy as np

candidates = np.array([[0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 1]])

syndromes = np.array([[0,0,0],
                      [0,0,0],
                      [0,0,0],
                      [0,0,0],
                      [0,0,0],
                      [0,0,0],
                      [0,0,0]])



# Counter for e bit sequence
counter = 0

# Base for random error
e = np.array([0,0,0,0,0,0])

# Create random error and add it to the e base
error_spot = np.random.randint(0, 6)
e[error_spot] = 1

# Word for encoding
m = np.array([0,0,1])


# Generation Matrix, contains Identity Matrix
G = np.array([[1, 0, 0, 1, 0, 1],
              [0, 1, 0, 1, 1, 1],
              [0, 0, 1, 0, 1, 1]])


# Parity-Check Matrix, contains Identity Matrix
H = np.array([[1, 1, 0, 1, 0, 0],
              [0, 1, 1, 0, 1, 0],
              [1, 1, 1, 0, 0, 1]])

# Calculate code word
codeword = np.dot(m, G)
codeword = np.mod(codeword, 2)
codeword = codeword.reshape(1,6)

# Add error to code word
r = np.add(codeword, e)
r = r.reshape(6,1)
r = np.mod(r, 2)

# Calculate parity-check matrix * r(transpose)
Hrt = np.dot(H, r)
Hrt = np.mod(Hrt, 2)


# Form syndromes
for o in range(0, 7):
    syndromes[o] = np.dot(H, candidates[o])

syndromes = np.transpose(syndromes)

# Go through H-chart and compare Hrt to it. Counter goes up every round if there is no equal value.
# When it finds equal, stops   
for i in range(len(syndromes[0,:])):
    
    if np.array_equal(syndromes[:,[i]], Hrt):
        counter = counter +1
        break
    else:
        counter = counter +1

# Candidate for error correction
X = candidates[counter - 1]

# Calculate C = r + X
r = r.reshape(1,6)
X = X.reshape(1,6)
C = np.add(r, X)
C = np.mod(C, 2)

# Print out the decoded word
print("Original code word is: ")
print(m)
print("Encoded word (incl. error):")
print(r)
print("Decoded word is:")
print(C[0, 0:3])






