#!/bin/awk
{
	w+=NF;
	c+=(length($0)+1);
}
END{print NR, w, c}
