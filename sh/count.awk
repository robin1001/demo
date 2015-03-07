#!/bin/awk
BEGIN {
	FS="[^a-zA-Z]"
}
{
	for(i=1; i<=NF; i++)
		words[tolower($i)]++;
}
END {
	delete words[""]
	for (x in words)
		print x, words[x];
}
