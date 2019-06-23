#!/bin/bash

domain="example.com"
home_di="/home/ubuntu/client-reflection"

lets_encrypt_home="/etc/letsencrypt/live"
access_log_file="$home_dir/access.log"
all_log_file="$home_dir/all.log"

private_key="$lets_encrypt_home/$domain/privkey.pem"
cert_file="$lets_encrypt_home/$domain/cert.pem"
ca_cert_file="$lets_encrypt_home/$domain/chain.pem"

gunicorn server:app --daemon --workers 2 --bind "0.0.0.0:443" --keyfile $private_key --certfile $cert_file --ca-certs $ca_cert_file --enable-stdio-inheritance --log-level=debug --access-logfile $access_log_file --log-file $all_log_file
