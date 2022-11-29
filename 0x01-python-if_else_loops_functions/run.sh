#!/bin/bash
chmod a+x *.py *.sh
ls
echo "Would you like to compile and/or run a file too?
Type the file name or *.extension: 
Type nvm to quit without running anything:"
read query
if [ "$query" != "nvm" ]; then
	if [[ "$query" == *".c"* ]]; then
		gcc -Wall -Werror -pedantic -std=gnu89 $query -o executable
		./executable
	elif [[ "$query" == *".py"* ]]; then
		./$query
	fi
fi
