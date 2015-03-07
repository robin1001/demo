#!/bin/bash

if [ -x if.sh ]; then
	echo "yes"
fi

if [ ! -d if.sh ]; then
	echo "not dir"
fi

if ! [ -d if.sh ]; then
	echo "not dir"
fi

a=3
if [ $a == 3 ]; then
	echo "eq";
fi

if [ $a -lt 4 ]; then
	echo "lt"
fi

if [ $a != 4 ]; then
	echo "ne"
fi
