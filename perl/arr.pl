#!/bin/env perl

@arr = (1, 2, 3, 4, 5);
print @arr,"\n";
print $#arr,"\n";
for ($i = 0; $i <= $#arr; $i++) {
	print $arr[$i], "\n";
}
push @arr, 6;
$last = pop @arr;
print $last, "\n";
$head = shift @arr;
print $head, "\n";
print $#arr, "\n";
print scalar @arr, "\n";

foreach $x (@arr) {
    print $x, " ";
}
print "\n";


%records = ("apple"=>2, "pear"=>1.5, "banana"=>1);
for $key (keys(%records)) {
    print $key, " ", $records{$key}, "\n"
}

$records{"orange"} = 0.5;
while (($key, $value) = each(%records)) {
    print $key, " ", $value, "\n";
} 
