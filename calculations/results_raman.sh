#!/bin/bash

# All analysis files will be stored one directory up
storage=$(pwd)/../
indiv=${storage}/RAMAN_RESULTS
mkdir $indiv

for i in */; do
	if [ -e ${i}/*normal ]; then
		mkdir ${indiv}/${i}
		cp ${i}*xyz ${indiv}/${i}		# Get structures
		cp ${i}*out ${indiv}/${i}		# Get output file (for normal mode analysis)
		cp ${i}*nw ${indiv}/${i}		# Get input script
		cp ${i}*normal ${indiv}/${i}		# get Raman results
	fi
done

# Tar results
cd ../
tar -czvf RESULTS_RAMAN.tar.gz RAMAN_RESULTS
