#!/bin/bash

#SBATCH --exclusive   
#SBATCH -t 2-0 
#SBATCH -A TG-TRA140037 
#SBATCH -p normal 
#SBATCH -N 1 
#SBATCH -n 16 
#SBATCH -J benchmarks_raman

module load nwchem


ibrun -np 16 nwchem calc.nw


