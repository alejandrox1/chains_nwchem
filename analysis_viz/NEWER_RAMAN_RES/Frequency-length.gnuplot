set ter pos landscape enhanced color solid lw 2
set out 'plot.ps'
set multiplot 

set format z "%10.3f"
set xtics 4

set xrange[1:51]

set ylabel "Frequency  (cm\^{-1})" 
set xlabel "n"

plot 'b-freq.txt' using 1:2 w p pt 7 lc rgb "black" title "no strain",  \
        '03p-freq.txt' using 1:2 with points pt 7 lc rgb "red" title "0.3% strain", \
        '1p-freq.txt' using 1:2 with points pt 7 lc rgb "blue" title "1.0% strain"


plot 'b-freq.txt' using 1:2 w l lc rgb "black" title "no strain",  \
	'03p-freq.txt' using 1:2 w l lc rgb "red" title "0.3% strain", \
	'1p-freq.txt' using 1:2 w l lc rgb "blue" title "1.0% strain"
