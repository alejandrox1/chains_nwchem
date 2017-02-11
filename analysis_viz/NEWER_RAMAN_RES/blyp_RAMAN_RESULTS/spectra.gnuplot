set ter pos landscape enhanced color solid lw 2
set out 'monomer_spectra.ps'
set multiplot

set format y "%1.1g"
set xtics 500

set ylabel "Intensity"
set xlabel "Frequency  (cm\^{-1})"

set size 1,1
set origin 0,0
set xrange[-100:]
plot 'monomer.normal' every ::num using 1:2 w l notitle

