#!/bin/bash

# In Bash (and ksh, zsh, dash, etc.), you can use parameter expansion with % which will remove characters from the
# end of the string or # which will remove characters from the beginning of the string. If you use a single one of 
# those characters, the smallest matching string will be removed. If you double the character, the longest will be removed.
#  $ a='hello:world'
#  $ b=${a%:*}
#  $ echo "$b"
#  hello
#  $ a='hello:world:of:tomorrow'
#  $ echo "${a%:*}"
#  hello:world:of
#  $ echo "${a%%:*}"
#  hello
#  $ echo "${a#*:}"
#  world:of:tomorrow


mkdir OPTIMIZED_CHAINS

for subdir in */; do
	cd $subdir

	name=${subdir%_*}					# Name of structure (e.g. c2)
	ls opt-* > optimized_strucs.txt				# Get all structures
	last_struct=`tail -n 1 optimized_strucs.txt`		# Get the latest one
	cp $last_struct ../OPTIMIZED_CHAINS/${name}.xyz	# Copy the best structure to the desired dir

	cd ../
done
