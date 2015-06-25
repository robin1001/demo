#!/bin/env perl

$str = "this is a good day, 12345, this";
if ($str =~ m/this/) {
	print "matched\n";
}
if ($str =~ s:this:that:g) {
	print $str, "\n";
}
