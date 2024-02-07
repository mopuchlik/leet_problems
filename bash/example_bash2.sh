#!/bin/bash

echo -n 'podaj liczbe 1: '
read l1

echo -n 'podaj liczbe 2: '
read l2

suma=$(($l1+$l2))
echo "$suma"

# less than or equal
# https://tldp.org/LDP/abs/html/comparison-ops.html
if [ $suma -le 10 ]
then
       echo "suma wynosi:  $suma"
else
       echo "suma jest > 10 (wynosi $suma) wiec nie ma printu"
fi