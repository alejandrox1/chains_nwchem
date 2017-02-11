#!/usr/bin/env python

import argparse
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Visalization of Normal Modes.')
parser.add_argument('-d','--dir', help='Name of directory (i.e., c20).', required=True)
parser.add_argument('-o','--orig', help='xyz structure file.', required=True)
parser.add_argument('-m','--mode', help='xyz structure file showing the displacement due to a normal mode.', required=True)
args = vars(parser.parse_args())

def refdist(x,y,z):
	dist = x**2.0 + y**2.0 + z**2.0
	return sqrt(dist)

def moveitem(lista):
	""" (list) -> list
	
	Flip the first and the third indices in a list.
	Check how are atoms connected in the xyz as opposed
	to in a visualization state.

	i.e., CCHH  ->  HCCH
	"""
	lista.insert(0, lista.pop(2))
	return lista

def difarrtolist(disp, init):
	"""(numpy.array) -> list

	Obtain the sums of each row of an array.
	"""
	elements = range(disp.shape[0])
	displacement = [0 for i in elements]
	for row in elements:
		dispd = refdist(disp[row,0], disp[row,1], disp[row,2])
		initd = refdist(init[row,0], init[row,1], init[row,2])
		displacement[row] = dispd - initd
	return displacement

def arrtolist(arr):
	"""(numpy.array) -> list

	Obtain the sums of each row of an array.
	"""
	elements = range(arr.shape[0])
	disp = [0 for i in elements]
	for row in elements:
		disp[row] = arr[row,:].sum()
	return disp

def toarray(filename):
	"""(str) -> np.array

	Reads XYZ file and saves coordinates to numpy array.

	contents of mol.xyz : 
	2
	geometry
	C                     0.00000000     0.00000000    -0.61354904
	C                     0.00000000     0.00000000     0.61354904

	>>> toarray('mol.xyz')
	[[ 0.          0.         -0.61354904]
	 [ 0.          0.          0.61354904]]
	"""    
	with open(filename, 'r') as f, open(filename, 'r') as n:    
		num_atoms = int(f.readline().strip())
		f.readline()
 
		xyz = np.zeros((num_atoms,3))        
		for idx, line in enumerate(f):
			# preprocess data from file
			line = line.split()
			line = line[1:]
			line = [float(i) for i in line]
			# Save data to numpy array
			xyz[idx,:] = line[:]
    
	return xyz

if __name__=="__main__":
	# Input files	
	init = toarray(args['orig'])
	disp = toarray(args['mode'])
	
	# Get total displacements
	#d = difarrtolist(disp, init)
	d = arrtolist((disp - init))
	d = [d[i+1]-d[i] for i in range(0,len(d)-1)]
	maxd = max(abs(i) for i in d)			# maximum displacement
	d = [(i/maxd) for i in d]			# normalize displacements
	d = moveitem(d)					# fix indices

	# plot displacements
	mode  = str(args['mode'][1:-4])
	plt.xticks(range(0, len(d)+1, 4))
	plt.ylim([-1,1])
	plt.title(r'%s cm$^1$' %mode, fontsize=16)
	plt.plot(range(1,len(d)), d[:-1], color='black', marker='o')
	plt.savefig('p'+mode, dpi=300)
	
