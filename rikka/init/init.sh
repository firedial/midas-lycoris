#!/bin/bash

mount -t cifs ${NAS_PATH} /mnt/nas -o username=${NAS_USER},password=${NAS_PASS},iocharset=utf8,rw

/usr/sbin/crond
crontab /home/root/init/crontab_setting
