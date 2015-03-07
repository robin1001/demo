#!/bin/env bash


echo $#
echo $1
echo $0

case $1 in
	--* ) echo "--$1";;
	--*=* ) echo "--*=*";;
	--*:* )	echo "--*:*";;
	* ) break;;
esac


