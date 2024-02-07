#!/bin/bash

# # get data

### Task is to create a new array as the difference of columns 3 and 2 (col count starts at 0)

# csv_file="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/M3/L2/arrays_table.csv"
# wget $csv_file

csv='./arrays_table.csv'
echo "Displaying full table: "
cat $csv

column_0=($(cut -d "," -f 1 $csv))
column_1=($(cut -d "," -f 2 $csv))
column_2=($(cut -d "," -f 3 $csv))

echo "Displaying the first column: ${column_0[@]}"

# input column len
len=$(cat $csv | wc -l)
echo "There are $len lines in the input file"

if [ $len -eq 0 ]
then
    echo 'input string is empty'
else
    # create new column
    column_3=("column_3")

    for ((i=1; i<$len; i++)); do
        column_3[$i]=$((column_2[$i] - column_1[$i]))
    done
fi

echo "Result: ${column_3[@]}"
