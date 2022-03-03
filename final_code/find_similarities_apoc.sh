#!/usr/bin/env bash
FILE1=${1?Error: no pocket 1 given}
FILE2=${2?Error: no pocket 2 given}

apoc $FILE1 $FILE2 | awk -F'[ :]+' '/TM-score /{print $3}'

