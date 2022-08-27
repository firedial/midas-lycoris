#!/bin/bash


if [ $1 = "0" ]; then
  MSG="OK!"
else
  MSG="${SLACK_USER} error!"
fi

DATA="{\"text\":\"${MSG}\"}"
curl -X POST -H 'Content-type: application/json' --data "${DATA}" ${SLACK_URL}

