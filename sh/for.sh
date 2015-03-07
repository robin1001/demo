#!/bin/env bash



for x in *; do
	if [ -f "$x" ]; then
		echo $x
	fi
done


for ((i=0; i<10; i++)); do
	echo $i
done


echo "paralize echo"

for ((i=0; i<10; i++));
do
{
	echo $i
}&
done

wait
