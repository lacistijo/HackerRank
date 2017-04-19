#!/usr/bin/perl

$a0_temp = <STDIN>;
@a0_arr = split / /,$a0_temp;
$a0 = $a0_arr[0];
chomp $a0; 
$a1 = $a0_arr[1];
chomp $a1;
$a2 = $a0_arr[2];
chomp $a2;
$b0_temp = <STDIN>;
@b0_arr = split / /,$b0_temp;
$b0 = $b0_arr[0];
chomp $b0; 
$b1 = $b0_arr[1];
chomp $b1;
$b2 = $b0_arr[2];
chomp $b2;
# Write Your Code Here

$a=0;
$b=0;

for($i=0; $i<3; $i++)
{
    if(@a0_arr[$i] > 100 || @b0_arr[$i] > 100)
    {
        print "Error! Value greater than 100";
    }
    elsif(@a0_arr[$i] > @b0_arr[$i])
    {
        $a++;
    }
    elsif(@b0_arr[$i] > @a0_arr[$i])
    {
        $b++;
    }
}

print "$a $b";