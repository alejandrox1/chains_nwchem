#!/bin/bash

#SBATCH --exclusive           # Individual nodes
#SBATCH -t 2-0                # Run time (hh:mm:ss)
#SBATCH -o slurm.%j.out

module load nwchem/6.5

# INPUT
n=$1

ibrun -np $n nwchem bp91-pcs0_acetylene.nw

