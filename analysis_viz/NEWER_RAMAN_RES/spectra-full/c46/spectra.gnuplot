set ter pos landscape enhanced color solid lw 2
set out 'c46_spectra.ps'
set multiplot

#set key at screen 0.5,screen 0.9 maxrows 2
set key right top
unset key
set format y "%1.1g"
set xtics 500

set ylabel "Intensity"
set xlabel "Frequency  (cm\^{-1})"

set size 1,1
set origin 0,0
set xrange[-100:]
plot "c46.normal" every ::152 using 1:2 w l lc rgb "black" title "no strain", "03pc46.normal" every ::152 using 1:2 w l lc rgb "blue" title "0.3% strain", "1pc46.normal" every ::152 using 1:2 w l lc rgb "red" title "1.0% strain"


set size 0.67,0.55
	set origin 0.3,0.4
	set key
	set xrange[1100:3500]
	set xlabel 
	set ylabel 
	plot 'c46.normal' every ::152 using 1:2 w l lc rgb 'black' title 'no strain', '03pc46.normal' every ::152 using 1:2 w l lc rgb 'blue' title '0.3% strain', '1pc46.normal' every ::152 using 1:2 w l lc rgb 'red' title '1.0% strain'