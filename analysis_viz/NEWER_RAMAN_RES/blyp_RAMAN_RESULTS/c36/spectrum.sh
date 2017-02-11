#!/bin/bash


lenght=$1       # lenght of chain
startn=$2       # Due to the formating for the raman output, one needs to input the line number to start reading from

cp ../spectra.gnuplot .

sed -i "s/monomer/c${lenght}/g" spectra.gnuplot
sed -i "s/num/${startn}/g" spectra.gnuplot

# Inset
if [ "${lenght}" -ge "20" ]; then
	echo "set size 0.67,0.55
	set origin 0.3,0.4
	set xrange[1100:3500]
	set xlabel ""
	set ylabel ""
	plot 'c${lenght}.normal' every ::${startn} using 1:2 w l notitle " >> spectra.gnuplot
fi

gnuplot spectra.gnuplot

# Move all files one directory up (main.tex)
cp c${lenght}_spectra.ps ../


