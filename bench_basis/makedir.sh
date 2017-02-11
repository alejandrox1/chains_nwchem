#!/bin/bash
#~ 
#~ Input: File with basis sets and the desired exchange correlation functional, in that order.
#~
#~ NOTE: This script doesn't handle directories with '/', hence these should be run manually.
#~

# File with available basis sets
basiss=$1
xcf=$2
# Exchange correlation functionals
case "$xcf" in
	"b3lyp") 
		func="b3lyp"
		;;
	"blyp")
		func="becke88 lyp"
		;;
	*)
                echo "Unkown option."
                exit
esac


# Create top directory for tests
mkdir "$xcf"
cd "$xcf"
pwd
cp ../${basiss} .

while IFS='' read -r line || [[ -n "$line" ]]; do

	# Get basis set from file
	nset=$line			# No spaces for directory naming
	sset=$line			# With spaces for nw naming
	# Get rid of white spaces
	set="$(echo -e "${nset}" | tr -d '[[:space:]]')"
	
	# Make directory for run
	if [ ! -d "$set" ]; then
		mkdir "$set"
		cd "$set"
		pwd
		# Get and modify the needed files (acetylene.nw and monomer.xyz)
		cp ../../acetylene.nw .
		cp ../../monomer.xyz .
		sed -i "s/library .*/library $sset/" acetylene.nw
		sed -i "s/xc .*/xc $func/" acetylene.nw

		# run calculation
		timeout 30m nwchem acetylene.nw > slurm.out
		#wait

		cd ..
	fi

done < "$basiss"

