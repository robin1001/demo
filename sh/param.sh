#!/bin/bash

#for ((i=1; i<=$#; i++)); do
#    echo ${!i}
#done

echo $0 $@

while true; do
    [ -z ${1:-} ] && break;
    
    case $1 in
    --*) name=`echo $1 | sed "s:^--::"`;
         echo $name:$2;
         eval $name=$2;
         shift 2;;
    *) break;;
    esac

done


