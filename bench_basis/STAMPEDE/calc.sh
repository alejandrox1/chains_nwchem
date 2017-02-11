#!/bin/bash

#SBATCH --exclusive           # Individual nodes
#SBATCH -t 0-00:30            # Run time (hh:mm:ss)
#SBATCH -J BASISSETS
#SBATCH -o slurm.%j.out

n=$1

module load nwchem

ibrun -np $n nwchem acetylene.nw 
