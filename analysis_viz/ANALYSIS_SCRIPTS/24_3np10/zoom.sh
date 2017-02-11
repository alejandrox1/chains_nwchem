#!/bin/bash


lenght=$1
startn=$2
cp ../zoom .

sed -i "s/monomer/c${lenght}/g" zoom

gnuplot zoom


cp c${lenght}_zoom.eps ../
cp c${lenght}_zoom.tex ../
