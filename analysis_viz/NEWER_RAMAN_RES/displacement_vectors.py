#!/usr/bin/env python

import argparse
import itertools
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


distance = lambda arr: sqrt( arr[0]**2.0 + arr[1]**2.0 + arr[2]**2.0 )

def skip_nlines(stream, n):
    for i in range(n):
        stream.readline()
    return

def read_geom(stream):
    """(stream) -> boolean, list

    Read the optimized geometry performed by NWCHEM.
    """
    delimiter = "---"
    skip_nlines(stream, 6)
    geom = []
    while True:
        line = stream.readline().strip()
        if delimiter not in line:
            geom.append(line.split())
        else:
            break
    geom = [x for x in geom if len(x)>2]
    geom = np.array(geom)
    geom = np.delete(geom, [0,1,2], axis=1)
    return geom

def read_modes(stream):
    """(stream) -> boolean, list

    Read all the information related to the vibrational analysis 
    performed by NWCHEM.
    """
    delimiter = "---"
    modesvec = []
    while True:
        line = stream.readline().strip()
        # stop when ...
        if delimiter not in line:
            modesvec.append(line.rstrip('\n').split())
        else:
            break

    return False, modesvec    

def get_nmodes(slurminput):
    """(file) -> int, numpy.array, list[list]

    Find the field describing the normal mode eigenvectors on the
    .out file. It only works for NWCHEM output files.

    Input:
        slurminput : name of slurm output file.

    Output:
        num_atoms : number of atoms.
        geometry : numpy array containing the atom coordinates.
        vibmodes : list of lists with output from slurm containing the
                   results from the vibrational analysis from NWCHEM.
    """
    xyz_header  = "XYZ format geometry"
    geom_header = "Geometry \"geometry\" -> \"geometry\""
    mode_header = "(Frequencies expressed in cm-1)"

    slurm = open(slurminput, 'r')
    
    field        = False
    stop_reading = False
    num_atoms    = 0
    geometry     = np.empty(0)
    vibmodes     = []
    for line in slurm:
        line = line.strip()
    
        if geom_header in line:                             # Get structure
            geometry = read_geom(slurm) 
            num_atoms = geometry.shape[0]   
        elif mode_header in line:                           # Look for beginning of NORMAL MODE EIGENVECTORS
            stop_reading, vibmodes = read_modes(slurm) 
        elif stop_reading:                                  # We found what we were looking for
            break
    slurm.close()
    
    # get rid of empty fields
    vibmodes = [line for line in vibmodes if line!=[]]
    
    return num_atoms, geometry.astype(float), vibmodes

def nmodes_proc(vibmodes, num_atoms):
    """(list[list], int) -> dict

    Parse the NWCHEM normal mode eigenvector output and separate the normal 
    modes from the frequencies into a more useful container.
    
    Input:
        vibmodes : list of lists containing the info from vibrational analysis (from slurm).
        num_atoms: number of atoms.

    Output:
        vecs : dictionary containing the vibrational frequencies as keys and a numpy
               array containing the corresponding eigenvector. 
    """
    # get the number of modes
    modesNd = vibmodes[::2+(3*num_atoms)]
    
    # get frequencies
    frequenciesNd = vibmodes[1::2+(3*num_atoms)]
    frequencies   = list(itertools.chain(*frequenciesNd))
    frequencies   = [entry for entry in frequencies if entry!='Frequency']
    frequencies   = [float(i) for i in frequencies]
    
    # get eigenvectors
    vectorsNd      = [x for x in vibmodes if (x not in modesNd) and (x not in frequenciesNd)]
    vectors        = np.array(vectorsNd)
    vectors        = np.delete(vectors, [0], axis=1)
    vectors        = vectors.astype(float)
    
    vecs = {}
    for f in range(len(frequencies)):
        N = 3*num_atoms
        i = int(f/vectors.shape[1])
        j = int(f%vectors.shape[1])
        vec = np.array(vectors[i*N:(i+1)*N, j])
    
        vecs[frequencies[f]] = vec
    return vecs

def arrtolist(arr, dist=False):
    """(numpy.array) -> list

    Obtain the sums of each row of an array by adding the 
    values or by adding the respetive distances of each atom.
    """
    elements = range(arr.shape[0])
    disp = [0 for i in elements]
    if dist:
        for row in elements:
            disp[row] = distance(arr[row,:])
    else:
        for row in elements:
            disp[row] = arr[row,:].sum()
    return disp

def moveitem(lista, ignh=False):
    """ (list) -> list
    
    Flip the first and the third indices in a list.
    Check how are atoms connected in the xyz as opposed
    to in a visualization state.

    i.e., CCHH  ->  HCCH
    """
    if ignh:
        lista.pop(0)
        lista.pop(-1)
    else:
        lista.insert(0, lista.pop(2))
    return lista

def visuzlization(mode, vec, show=False):
    """((str,float), numpy.array, numpy.array) -> None

    Display th normalized distance between consequent links in a carbon chain.

    INPUT:
        mode : identifying a vibrational mode.
        displacement : displacement vector.
        equil : optimized molecular geometry. 
        show : True -> show on screen, else save.
    """
    vec  = np.reshape(vec, (int(vec.shape[0]/3),3))
    vecmax = np.empty(vec.shape[0])
    for row in range(vec.shape[0]):
        vecmax[row] = max(vec[row], key=abs)
    maxd = max(vecmax.min(), vecmax.max(), key=abs) 
    vecmax  = vecmax/maxd 

    plt.figure() 
    plt.xticks(range(1, vecmax.shape[0]+1, 4))
    plt.ylim([-1,1])
    plt.title(r'%s cm$^{-1}$' %mode, fontsize=16)
    plt.plot(range(1, vecmax.shape[0]+1), vecmax, color='black', marker='o')
    if not show:
        plt.savefig('p'+str(mode)[:-2]+'pdf', dpi=300)
    else:
        plt.show()
    plt.close()
    return 



if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Visalization of Normal Modes.')
    parser.add_argument('-i','--input', help='Name of slurm.%j.out (output) file.', required=True)
    args = vars(parser.parse_args())

    num_atoms, geom, info = get_nmodes(args['input'])       # Parse slurm file get number of atoms, coordinates, and vibrational output
    vecs = nmodes_proc(info, num_atoms)                     # Process the vibrational modes output

    for freq, vec in vecs.items():
        if 1000 <= freq <= 3000:
            disp = visuzlization(freq, vec)    # Visualization
