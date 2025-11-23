#!/bin/bash

OUTPUT="s18_q2_writemask.txt" #The file to the store output

{
    echo "Username: $(whoami)"
    echo "Hostname: $(hostname)"
    echo "Files without write permission:"
    find . -type f ! -perm /222 -printf "%p\n"
} > "$OUTPUT"
