#!/bin/env perl
$file_name = 'test.txt';
open($fid, '>', $file_name) or die;
print $fid "file test\n";
close $fid;

$csv_file = 'data.csv';
open($csv, '<', $csv_file) or die;
while ($line = <$csv>) {
	print $line;
	chomp $line;
	@arr = split ",", $line;
	for ($i = 0; $i <= $#arr; $i++) {
		print $arr[$i], "\n";
	}
}
