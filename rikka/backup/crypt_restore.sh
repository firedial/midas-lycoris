#!/bin/sh

BACKUP_DIR="/mnt/nas/midas/crypt"
ENCRYPTED_BACKUP_FILE_NAME=$(ls -r1 ${BACKUP_DIR} | head -n 1)

openssl aes-256-cbc -d -pbkdf2 -iter 100000 -salt -in ${BACKUP_DIR}/${ENCRYPTED_BACKUP_FILE_NAME} -out /tmp/restore.dump.gz -pass env:ENCRYPTION_KEY
gunzip /tmp/restore.dump.gz

/usr/bin/mysql -u ${DB_MIDAS_ROOT_USER} -p${DB_MIDAS_ROOT_PASS} -h ${DB_HOST} ${DB_DATABASE_NAME} < /tmp/restore.dump
rm /tmp/restore.dump
