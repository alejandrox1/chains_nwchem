#!/bin/bash


lenght=$1 	# lenght of chain
startn=$2	# Due to the formating for the raman output, one needs to input the line number to start reading from
cp ../rs .

sed -i "s/monomer/c${lenght}/g" rs
sed -i "s/num/${startn}/g" rs

gnuplot rs

# Move all files one directory up (main.tex)
cp c${lenght}_rs.eps ../
cp c${lenght}_rs.tex ../
