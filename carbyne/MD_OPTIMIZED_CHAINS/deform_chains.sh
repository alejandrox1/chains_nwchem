#!/bin/bash

cp ../p_strain.py .

for i in {2..50..2}; do 
	if [ -f "c${i}.xyz" ]; then
		echo "c${i}.xyz"
		python p_strain.py c${i}.xyz 3.0; python p_strain.py c${i}.xyz 0.3; python p_strain.py c${i}.xyz 0.03
	fi
done
