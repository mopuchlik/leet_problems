#!/bin/bash

echo -n 'wybierz tak albo nie: '
read response

if [ $response == 'nie' ] ||  [ $response == 'tak' ]
then
        echo -n "odpowiedz: $response"  
else
        echo -n 'musisz napisac tak albo nie'
fi
