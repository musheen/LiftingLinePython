########################################################################
#
# Lifting Line Theory Test Code
#
# Author: Oisin Tong
#
# Date: 30/09/2017
#
# Revision: 1.0
#
########################################################################

print "\n"
print "//------------------------------------------------------------//"
print "//             Lifting Line Theory Test Code                  //"
print "//             Author: Oisin Tong                             //"
print "//             Revision: 1.0                                  //"
print "//------------------------------------------------------------//"
print "\n"

#
# Some Notes:
# I have used a zero based array system. 
# I used Philips as a reference guide, and he uses a 1 based system
#

#-------------------------------- Import ------------------------------#

#
# Import any packages you need here
#

import numpy as np
import scipy
from math import *
from matplotlib import pyplot as plt
import sys

#------------------------------ Initialize ----------------------------#

#
# Initializing info
#

# pi 
pi = 4.*atan(1.)

# number of points on wing
N 	= 99

#----------------------------- Airfoil Info ---------------------------#

#
# Put all the airfoil information here
#

# lift slope
CLa  	= 2.*pi

# lift at zero angle of attack
CL0 	= 0.


#------------------------------ Wing Info -----------------------------#

#
# Put all the wing information here
#


# span
b 	= 4.

# planform area 
S 	= 2.

# aspect ratio
AR 	= b*b/S

# tip chord ratio
TR 	= 1.

# root chord
cRoot = 0.5

# number of points on wing
N 	= 7

# chord length
c 	= np.ones(N)
for i in range (0,N):
    c[i] = 0.5


# find points along wing
th 	= np.zeros(N)
for i in range (0,N):
    th[i] = (i)*pi/(N-1.) 

#print th    

print "---------------------------------------------------------------------"
print " Wing Characteristics"
print "---------------------------------------------------------------------"

print " Wing Aspect Ratio: ", AR
print " Tip-Chord Ratio: ", TR
print "---------------------------------------------------------------------"
print "\n"

#--------------------------- Calculate C Matix ------------------------#

#
# C matrix controls all the lift calculations
#


# initialize array
C 	= np.zeros((N,N))


# wingtips
for j in range (0,N):
    C[0,j] = (j+1)*(j+1)

# interior portion
for i in range (1,N-1):
    for j in range (0,N):
        p1 = 4.*b/(CLa*c[i])
        p2 = (j+1)/sin(th[i])
        p3 = (p1+p2)*sin((j+1.)*th[i])
        C[i,j] = p3

# wingtips
for j in range (0,N):
    C[N-1,j] = (j+1)*(j+1)*pow(-1.,j+2)


#print C

# inverse of C
Ci 	= np.linalg.inv(C)

#print "\n"
#print Ci

#-------------------------------- a Array -----------------------------#

# initialize array
aa 	= np.ones(N)

# calculate a array
a 	= np.dot(Ci,aa)


#---------------------------- Optimum Washout -------------------------#

# initialize array 
omega = np.zeros(N)

for i in range (0,N):
    omega[i] = 1. - sin(th[i])/(c[i]/cRoot)

#print omega


#-------------------------------- b Array -----------------------------#

# calculate b array
b 	= np.dot(Ci,omega)

#-------------------------------- c Array -----------------------------#


#-------------------------------- d Array -----------------------------#



#-------------------------------- Factors -----------------------------#

print "---------------------------------------------------------------------"
print " Aerodynamic Factors"
print "---------------------------------------------------------------------"

# lift slope factor
p1 	= 1.-(1.+pi*AR/CLa)*a[0]
p2    = (1.+pi*AR/CLa)*a[0]
KL 	= p1/p2
print " Lift Slope Factor = ", KL

# induced drag factor
KD 	= 0.
for i in range (1,N):
    KD = KD + (i+1)*(a[i]*a[i])/(a[0]*a[0])
print " Induced Drag Factor = ", KD

# lift-washout contribution to induced drag factor
KDL 	= 0.
for i in range (1,N):
    KDL = KDL + (i+1)*(a[i]/a[0])*(b[i]/b[0]-a[i]/a[0])
KDL 	= KDL*2.*b[0]/a[0]
print " Lift-Washout Contribution to Induced Drag Factor = ", KDL

# washout contribution to induced drag factor
KDW 	= 0.
for i in range (1,N):
    KDW = KDW + (i+1)*(b[i]/b[0]-a[i]/a[0])*(b[i]/b[0]-a[i]/a[0])
KDW 	= KDW*(b[0]/a[0])*(b[0]/a[0])
print " Washout Contribution to Induced Drag Factor = ", KDW

# optimum induced drag factor
KDo 	= KD - KDL*KDL/(4.*KDW)
print " Optimum Induced Drag Factor = ", KDo

# span efficiency factor
Es 	= 1./(1.+KD)
print " Span Efficiency Factor = ", Es


print "---------------------------------------------------------------------"
print "\n"

#----------------------------- Coefficients ---------------------------#

print "---------------------------------------------------------------------"
print " Aerodynamic Coefficients"
print "---------------------------------------------------------------------"

# max total washout
W 	= 

# true lift slope
CLA 	= CLa/((1.+CLa/(pi*AR))*(1.+KL))
print " Lift Slope = ",CLA

# lift
alpha = 5.
aL0	= 0.
CL 	= CLA*(alpha - aL0)
print " Lift = ",CL

# lift induced drag
CDi 	= CL*CL/(pi*AR*Es)
print " Lift Induced Drag = ",CDi

print "---------------------------------------------------------------------"
print "\n"

#------------------------------ Initialize ----------------------------#
#------------------------------ Initialize ----------------------------#
#------------------------------ Initialize ----------------------------#




#--------------------------------- Plot -------------------------------#

#
# Plot the final information here
#





#---------------------------------- End -------------------------------#


