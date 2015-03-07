#!/bin/awk

BEGIN {
	while(getline < "if.sh")
		print $0;
}
{
	print NR, $0;
}
