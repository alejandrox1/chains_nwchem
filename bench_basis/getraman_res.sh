#!/bin/bash

touch freq_positions.txt

for i in */; do
	cd "$i"
	if [ -s "c2h2.normal" ]
		freq=`awk 'NR==17{print $2}' c2h2.normal`
		echo "$i          $freq"  >> ../freq_positions.txt
	fi
	cd ../
done
