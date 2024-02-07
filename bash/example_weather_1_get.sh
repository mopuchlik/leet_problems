#!/usr/bin/bash

header=$(echo -e "year\tmonth\tday\tobs_tmp\tfc_temp")
echo $header > rx_poc.log

# set date
today=$(date '+%Y%m%d')

# set name of downloaded raw data file
weather_report=raw_data_$today

# set folder
weather_folder=/home/michal/Pulpit

# set city
city=Casablanca

# download raw data
curl wttr.in/${city} --output ${weather_folder}/${weather_report}

grep °C ${weather_folder}/${weather_report} > temperatures.txt

# note: head/tail -3 is the same as head/tail -n 3
# note cut -d "x" divides string by "x" delimiter
# extract the current temperature
obs_tmp=$(cat -A temperatures.txt | head -1 | cut -d "m" -f5 | cut -d "+" -f2 | cut -d "^" -f1 )
echo "observed temperature = $obs_tmp"

# extract the current temperature
fc_tmp=$(cat -A temperatures.txt | head -3 | tail -1 | cut -d "m" -f4 | cut -d "+" -f2 | cut -d "^" -f1 )
echo "forecated temperature = $fc_tmp"

# set local time variables
hour=$(TZ='Morocco/Casablanca' date -u +%H)
day=$(TZ='Morocco/Casablanca' date -u +%d)
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)

echo -e "$year\t$month\t$day\t$obs_tmp\t$fc_tmp" >> rx_poc.log
