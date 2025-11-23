#!/bin/bash

OUTPUT_FILE="top3_output.log"
INTERVAL=5
TOTAL=120

echo "Logging top 3 CPU processes every $INTERVAL sec for $TOTAL sec" > "$OUTPUT_FILE"
echo "------------------------------------------------------------" >> "$OUTPUT_FILE"

END=$((SECONDS + TOTAL))

while [ $SECONDS -lt $END ]; do
    {
        echo ""
        echo "===== Timestamp: $(date) ====="
        ps -eo pid,ppid,cmd,%cpu --sort=-%cpu | head -n 4
    } >> "$OUTPUT_FILE"
    
    sleep $INTERVAL
done
