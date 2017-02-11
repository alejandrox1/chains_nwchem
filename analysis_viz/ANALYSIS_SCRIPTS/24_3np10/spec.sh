#!/bin/bash


lenght=$1
startn=$2
cp ../rs .

sed -i "s/monomer/c${lenght}/g" rs
sed -i "s/num/${startn}/g" rs

gnuplot rs


cp c${lenght}_rs.eps ../
cp c${lenght}_rs.tex ../
