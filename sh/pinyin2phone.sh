#!/bin/bash

if [ $# -ne 2 ]; then
	echo "Usage: pinyin2phone.sh dict_file pinyin2phone"
	exit -1
fi

echo $*
dict=$1
awk -v phone_map=$2 \
'BEGIN {
	while (getline < phone_map) {
		t = "";
		for (i=2; i<=NF; i++)
			t = t " " $i;
		map[$1] = t;
		#print $1, t
	}
}
{
	line = $1;
	for (i=2; i<=NF; i++)
		line = line " " map[$i];
	print line;
}
' $dict 

