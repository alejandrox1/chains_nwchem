#!/bin/bash

cp /home/alarcj/origami_physics/physics/research/NWCHEM/JUNE_RAMAN_RES/harmonic_viz.py .

for mode in m*;
do
	echo ${mode}
	python3 harmonic_viz.py -o opt-003.xyz -m ${mode}
done


