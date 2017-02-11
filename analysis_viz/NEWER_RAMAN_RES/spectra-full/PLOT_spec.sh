#!/bin/bash

c=$1
#s=$(( 20 + 4 * $c))
s=$2

cp ../spectrum.sh .
cp ../../blyp_RAMAN_RESULTS/c${c}/c${c}.normal .
cp ../../03p-blyp_RAMAN_RESULTS/c${c}/p0.3_c${c}.normal 03pc${c}.normal
cp ../../1p-blyp_RAMAN_RESULTS/c${c}/p1.0_c${c}.normal 1pc${c}.normal

bash spectrum.sh ${c} ${s}; gnome-open c${c}_spectra.ps
