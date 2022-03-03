#!/usr/bin/env bash
FILE1=${1?Error: no pocket 1 given}
FILE2=${2?Error: no pocket 2 given}

#echo "Python has finished"
test="$(python3 neib_kinases.py $FILE1 $FILE2)"
#echo "Python has finished"
#echo "test = $test"

if [[ $test -eq 1 ]]
then
  apoc $FILE1 $FILE2 | awk -F'[ :]+' '/TM-score /{print $3}'
else
  echo "0"
fi
