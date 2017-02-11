#!/bin/bash

for dir in */;
do
	cd $dir
    echo $dir
	cp /home/alarcj/origami_physics/physics/research/NWCHEM/JUNE_RAMAN_RES/displacement_vectors.py .

    slurm=`ls -ltr *out | tail -n 1 | awk '{print $NF}'`
    python3 displacement_vectors.py -i $slurm

	cd ../
done


