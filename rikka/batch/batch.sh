#!/bin/sh

sh $1

if [ $? -eq 0 ]; then
  # success
  sh /home/root/batch/alert.sh 0
else
  # failed
  sh /home/root/batch/alert.sh 1
fi


