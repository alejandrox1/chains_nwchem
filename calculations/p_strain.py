#!/usr/bin/env python

#~	python2 p_strain.py cX.xyz percentdeformation
#~
#~	Will output (p/n)percentdeformation_cX.xyz
#~
#~ This script was written with the desired to modify a given XYZ formatted file and apply strain
#~ to the system. Note: this is only for one dimensional chains.
#~
#~ We will find a numerical approximation to the amount of deformation needed to obtain the desired amount of strain.
#~ Keep in mind that we are using the percentage of displacement as the parameter of comparison, we can modify the number 
#~ od decimal places in order to change the degree of agreement. 
#~ As an estimate the fluctuations of a C-C bond is less than 1%. 
#~ "Tables of bond lengths determined by X-ray and neutron diffraction. Part 1. Bond lengths in organic compounds"
#~ F. H. Allen, O. Kennard, D. G. Watson, L. Brammer, A. G. Orpen. J. Chem. Soc., Perkin Trans. 2, 1987, S1-S19. 
#~ DOI: 10.1039/P298700000S1 

import sys
import numpy as np
from math import sqrt

## INPUT file
coorfile = str(sys.argv[1])		# XYZ input file.
strain_in= float(sys.argv[2])		# Desired strain (percentage).
# precisison
# One would expect some balance between 'pres' (the number of decimals and the magnitud of fudgea/b.
pres=7					# 0.00003 -> 0.003 ( this should at least be 3 ) Rounding up answers during iteration process.
fudgea=1.00001				# Chainging these two parameters should only affect the speed of convergence.
fudgeb=0.9999				#

strain=(strain_in/100.0)

## READ 
matrix = np.genfromtxt(coorfile, dtype=("|S1", float, float, float), skip_header=2, names=('atoms', 'x', 'y', 'z')) 

# Read all carbon atoms to thedictionary c_positions and count the number of carbons
# Recall that Dictionaries do not preserve order
N_c=0
N_h=0
c_positions = {}
h_positions = {}
for row in range(len(matrix['atoms'])):
	if matrix['atoms'][row].decode('ascii')=='C':
		N_c += 1		
		c_positions[row] = [matrix['x'][row], matrix['y'][row], matrix['z'][row]]
	elif matrix['atoms'][row].decode('ascii')=='H':
		h_positions[row] = [matrix['x'][row], matrix['y'][row], matrix['z'][row]]	


# Get the carbon atoms that are at the edges
Cids = list(c_positions.keys())
Hids = list(h_positions.keys())
firstC = c_positions[min(Cids)]
lastC = c_positions[max(Cids)]

# Calculate the length of the chain
distance = sqrt((matrix['x'][Cids[0]]-matrix['x'][Cids[-1]])**2.0 + (matrix['y'][Cids[0]]-matrix['y'][Cids[-1]])**2.0 + (matrix['z'][Cids[0]]-matrix['z'][Cids[-1]])**2.0)
# BOND DISTANCES
cc_f = sqrt((matrix['x'][Cids[0]]-matrix['x'][Cids[1]])**2.0 + (matrix['y'][Cids[0]]-matrix['y'][Cids[1]])**2.0 + (matrix['z'][Cids[0]]-matrix['z'][Cids[1]])**2.0)
cc_l = sqrt((matrix['x'][Cids[-2]]-matrix['x'][Cids[-1]])**2.0 + (matrix['y'][Cids[-2]]-matrix['y'][Cids[-1]])**2.0 + (matrix['z'][Cids[-2]]-matrix['z'][Cids[-1]])**2.0)

pos_def = distance + (distance * strain)
neg_def = distance - (distance * strain)



## DEFORMATION
# Find main displacement direction
x = abs(np.std(matrix['x'])); y = abs(np.std(matrix['y'])); z = abs(np.std(matrix['z']))
if (x > y) and (x > z):
	maxid = 'x'
elif (y > x) and (y > z):
	maxid = 'y'
else:
	maxid = 'z'

# POSITIVE STRAIN
fudge=1.0
disp=0.0
deform1 = strain * cc_f
deform2 = strain * cc_l
while disp!=round(pos_def, pres):
        pos = np.genfromtxt(coorfile, dtype=("|S1", float, float, float), skip_header=2, names=('atoms', 'x', 'y', 'z'))
       
        if pos[maxid][min(Hids)]<0: 
                # Displace the last two H atoms in the matrix by the desired level of strain
                pos[maxid][min(Hids)] = pos[maxid][min(Hids)] - (deform1/2.0)
                pos[maxid][max(Hids)] = pos[maxid][max(Hids)] + (deform2/2.0)
                # Displace the last two C atoms in the matrix by the desired level of strain
                pos[maxid][min(Cids)] = pos[maxid][min(Cids)] - (deform1/2.0)
                pos[maxid][max(Cids)] = pos[maxid][max(Cids)] + (deform2/2.0)
        else:
                # Displace the last two H atoms in the matrix by the desired level of strain
                pos[maxid][min(Hids)] = pos[maxid][min(Hids)] + (deform1/2.0)
                pos[maxid][max(Hids)] = pos[maxid][max(Hids)] - (deform2/2.0)
                # Displace the last two C atoms in the matrix by the desired level of strain
                pos[maxid][min(Cids)] = pos[maxid][min(Cids)] + (deform1/2.0)
                pos[maxid][max(Cids)] = pos[maxid][max(Cids)] - (deform2/2.0)

	# change of the toal change length after modification
        displacement = sqrt((pos['x'][Cids[0]]-pos['x'][Cids[-1]])**2.0 + (pos['y'][Cids[0]]-pos['y'][Cids[-1]])**2.0 + (pos['z'][Cids[0]]-pos['z'][Cids[-1]])**2.0)
        disp = round(displacement, pres)
        percentage = abs((displacement-distance)/distance)	
	
        if disp<pos_def:
                fudge *= fudgea
        else:
                fudge = fudgeb
        deform1 *= fudge
        deform2 *= fudge
        #print(distance, round(pos_def, pres), disp, fudge, percentage, strain)
print("Original distance : %1.7f\nNew distance : %1.7f\n" %(distance, displacement))


# NEGATIVE STRAIN
fudge=1.0
disp=0.0
deform1 = strain * cc_f
deform2 = strain * cc_l
while disp!=round(neg_def, pres):
        neg = np.genfromtxt(coorfile, dtype=("|S1", float, float, float), skip_header=2, names=('atoms', 'x', 'y', 'z'))
      
        if neg[maxid][min(Hids)]<0:
                # Displace the last two H atoms in the matrix by the desired level of strain
                neg[maxid][min(Hids)] = neg[maxid][min(Hids)] + (deform1/2.0)
                neg[maxid][max(Hids)] = neg[maxid][max(Hids)] - (deform2/2.0)
                # Displace the last two C atoms in the matrix by the desired level of strain
                neg[maxid][min(Cids)] = neg[maxid][min(Cids)] + (deform1/2.0)
                neg[maxid][max(Cids)] = neg[maxid][max(Cids)] - (deform2/2.0)
        else:
                # Displace the last two H atoms in the matrix by the desired level of strain
                neg[maxid][min(Hids)] = neg[maxid][min(Hids)] - (deform1/2.0)
                neg[maxid][max(Hids)] = neg[maxid][max(Hids)] + (deform2/2.0)
                # Displace the last two C atoms in the matrix by the desired level of strain
                neg[maxid][min(Cids)] = neg[maxid][min(Cids)] - (deform1/2.0)
                neg[maxid][max(Cids)] = neg[maxid][max(Cids)] + (deform2/2.0)


        displacement = sqrt((neg['x'][Cids[0]]-neg['x'][Cids[-1]])**2.0 + (neg['y'][Cids[0]]-neg['y'][Cids[-1]])**2.0 + (neg['z'][Cids[0]]-neg['z'][Cids[-1]])**2.0)
        disp = round(displacement, pres)
        percentage = abs((displacement-distance)/displacement)

        if disp<neg_def:
                fudge = fudgeb
        else:
                fudge *= fudgea 
        deform1 *= fudge
        deform2 *= fudge
	#print(distance, round(neg_def, pres), disp, fudge, percentage, strain)
print("Original distance : %1.7f\nNew distance : %1.7f\n" %(distance, displacement))



## OUPUT
# create XYZ with positive strain
coorout1 = "p"+str(strain_in)+"_"+coorfile 
out = open(coorout1, 'w')
out.write('%d\n' % len(pos['atoms']))
out.write("\tpositive strain\n")
for row in range(len(pos['atoms'])):
        out.write('%s \t %1.8f \t %1.8f \t %1.8f\n' %(pos['atoms'][row].decode('ascii'), pos['x'][row], pos['y'][row], pos['z'][row]))
out.close()

# Create XYZ with negative strain
coorout1 = "n"+str(strain_in)+"_"+coorfile 
out = open(coorout1, 'w')
out.write('%d\n' % len(neg['atoms']))
out.write("\tpositive strain\n")
for row in range(len(neg['atoms'])):
        out.write('%s \t %1.8f \t %1.8f \t %1.8f\n' %(neg['atoms'][row].decode('ascii'), neg['x'][row], neg['y'][row], neg['z'][row]))
out.close()


