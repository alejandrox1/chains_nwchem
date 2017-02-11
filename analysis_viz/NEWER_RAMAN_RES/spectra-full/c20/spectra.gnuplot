set ter pos landscape enhanced color solid lw 2
set out 'c20_spectra.ps'
set multiplot
set key font ",18"
set xlabel font ",16"
set ylabel font ",16"  

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
plot "c20.normal" every ::75 using 1:2 w l lc rgb "black" title "no strain", "03pc20.normal" every ::75 using 1:2 w l lc rgb "blue" title "0.3% strain", "1pc20.normal" every ::75 using 1:2 w l lc rgb "red" title "1.0% strain"


set size 0.67,0.55
	set origin 0.3,0.4
	set key
	set xrange[1100:3500]
	set xlabel 
	set ylabel 
	plot 'c20.normal' every ::75 using 1:2 w l lc rgb 'black' title 'no strain', '03pc20.normal' every ::75 using 1:2 w l lc rgb 'blue' title '0.3% strain', '1pc20.normal' every ::75 using 1:2 w l lc rgb 'red' title '1.0% strain'
