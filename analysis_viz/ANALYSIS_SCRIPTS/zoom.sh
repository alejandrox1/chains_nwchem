#!/bin/bash

# This script was created to zoom in into a particular region of the raman/IR spectra

lenght=$1
cp ../zoom .

sed -i "s/monomer/c${lenght}/g" zoom

gnuplot zoom


cp c${lenght}_zoom.eps ../
cp c${lenght}_zoom.tex ../
