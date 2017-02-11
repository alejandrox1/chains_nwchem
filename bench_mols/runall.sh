#!/bin/bash

for i in */; do
	cd $i

	for j in */; do
		cd $j

		nwchem calc.nw > slurm.out

		cd ../
	done
	cd ../
done
