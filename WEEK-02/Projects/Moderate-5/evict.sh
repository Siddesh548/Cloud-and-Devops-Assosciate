#!/bin/bash

LOGFILE="/home/siddu/s18_q5_eviction.txt"
touch $LOGFILE
chmod 644 $LOGFILE

# Set Redis memory limit and eviction policy
redis-cli CONFIG SET maxmemory 1mb
redis-cli CONFIG SET maxmemory-policy allkeys-lru
redis-cli FLUSHALL

# Fulling Redis with many keys
for i in {1..100}; do
    redis-cli SET key$i val$i > /dev/null
done

Username=$(whoami)
Hostname=$(hostname)
EVIC=$(redis-cli INFO stats | grep evicted_keys | awk -F: '{print $2}')
echo "$(date '+%F %T') |user:$Username |host:$Hostname |evicted_keys:$EVIC" > $LOGFILE
