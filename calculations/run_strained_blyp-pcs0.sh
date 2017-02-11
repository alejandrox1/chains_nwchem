#!/bin/bash

#-      bash run_strained_blyp-pcs0.sh -N 1 -np 16 -c 2 -d p -s 3.0 
#-      bash run_strained_blyp-pcs0.sh -N numbernodes -np numberoftasks -c chainlength -d (p || n) -s strain(percentage)
#-
#- 	comet has 24 nodes per core.
#-      stampede has 16 nodes per core.

# ALLOCATIONS
xsede=TG-TRA140037
terro=TG-DMR160090

# INPUT
while [[ $# > 1 ]]; do
        key="$1"

	case $key in
        	-N|--nodes)
            	nodes="$2"
            	shift # past argument
            	;;
            	-np|--procs)
            	procs="$2"
            	shift # past argument
            	;;
            	-c|--chain)
            	length="$2"
            	shift # past argument
            	;;
		-d|--straindir)
                straindir="$2"
                shift # past argument
                ;;
		-s|--strain)
                strain="$2"
                shift # past argument
                ;;
            	*)
		echo "Unkown option."
                exit
                    # unknown option
         	;;
        esac
        shift # past argument or value
done
echo "bash run_strained_blyp-pcs0.sh -N $nodes -np $procs -c $length -d $straindir -s $strain" > README

# Determine the host
host=$(hostname)
set -- "$host"
IFS="."; declare -a array=($*)
echo "${array[@]}"
flag="${array[1]}"

case "$flag" in
        "stampede")
                cluster="$flag"
		partition=normal
		cpern=16
		
		echo "Running on sampede.tacc.xsede.org"

		runfiles=/scratch/03561/alarcj/NWCHEM
		structures=/scratch/03561/alarcj/NWCHEM/OPTIMIZED_CHAINS
		cp ${runfiles}/raman_run_strained_blyp-pcs0.sh .
		cp ${runfiles}/restart_raman.sh .
		cp ${runfiles}/strained_blyp-pcs0_acetylene.nw .
		cp ${runfiles}/acetylene_restart.nw .
		cp ${structures}/"${straindir}${strain}_c${length}.xyz" .
		;;
        "sdsc")
                cluster=comet
                files=/oasis/scratch/comet/alarcj/temp_project/AMINO/data/op_run
                partition=compute
                echo "Running on comet.sdsc.xsede.org"
                ;;
        *)
                echo "Unkown option."
                exit
esac

# Proper Naming
if [ "$length" -ne "2" ]; then
	numatoms=`awk 'NR==1{print $1}' "${straindir}${strain}_c${length}.xyz"`
	lastC=$(( $numatoms - 1 ))
	sed -i "s/atom 1 2.*/atom 1 ${lastC}/" strained_blyp-pcs0_acetylene.nw
fi
sed -i "s/monomer/${straindir}${strain}_c${length}/g" strained_blyp-pcs0_acetylene.nw
sed -i "s/monomer/${straindir}${strain}_c${length}/g" acetylene_restart.nw


sbatch -A $xsede -p $partition -N $nodes -n $procs -J ${straindir}c${length} raman_run_strained_blyp-pcs0.sh $procs > submit.txt
id=`awk 'END {print $NF}' submit.txt`
sbatch -A $xsede --dependency=afterok:${id} -p $partition -N $nodes -n $procs -J ${straindir}c${length} restart_raman.sh $procs



# FOR debugging purposes
echo "Allocated: $nodes nodes and $procs cores." >> README
echo "${straindir}${strain}_c${length}.xyz is being used." >> README 
echo "Check that ${id} is the same id as in submit.txt" >> README
