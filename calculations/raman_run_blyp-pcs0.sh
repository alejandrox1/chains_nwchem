#!/bin/bash

#SBATCH --exclusive           # Individual nodes
#SBATCH -t 2-0                # Run time (hh:mm:ss)
#SBATCH -o slurm.%j.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=alarcj137@gmail.com

module load nwchem/6.5

# INPUT
n=$1

ibrun -np $n nwchem blyp-pcs0_acetylene.nw

