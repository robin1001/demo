#!/bin/bash
a=(1 2 3 4)
echo ${#a[*]}
echo ${a[2]}
echo ${a[*]}
declare -A word
i=0
while read line && [ $i -lt 5 ]; do
  echo line
done  
