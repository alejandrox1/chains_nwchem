#!/bin/bash

c=$1
#s=$(( 20 + 4 * $c))
s=$2

cp ../spectrum.sh .

bash spectrum.sh ${c} ${s}; gnome-open c${c}_spectra.ps
