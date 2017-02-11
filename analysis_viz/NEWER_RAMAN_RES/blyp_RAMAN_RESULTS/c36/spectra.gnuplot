set ter pos landscape enhanced color solid lw 2
set out 'c36_spectra.ps'
set multiplot

set format y "%1.1g"
set xtics 500

set ylabel "Intensity"
set xlabel "Frequency  (cm\^{-1})"

set size 1,1
set origin 0,0
set xrange[-100:]
plot 'c36.normal' every ::121 using 1:2 w l notitle

set size 0.67,0.55
	set origin 0.3,0.4
	set xrange[1100:3500]
	set xlabel 
	set ylabel 
	plot 'c36.normal' every ::121 using 1:2 w l notitle 
