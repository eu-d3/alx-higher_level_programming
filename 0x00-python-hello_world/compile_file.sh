#!/bin/bash
echo"Here is a list of files, you can complile"
ls *.c 
echo "This script compiles only single C programs,
Which file would you like to compile at the moment: "
read file_name
if [ "$file_name" != "nvm" ]; then
	gcc -Wall -Werror -pedantic -std=gnu89 $file_name -o run_exec
	./run_exec
fi
