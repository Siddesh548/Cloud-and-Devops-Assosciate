#!/bin/bash

TARGET_DIR="./corrupt-files"

mkdir -p "$TARGET_DIR"

FILES=("config1.tmp" "config2.tmp" "testA.conf" "testB.conf" "randomfile.txt")

echo "Creating files with NO write and NO execute permissions..."

for file in "${FILES[@]}"; do
    touch "$TARGET_DIR/$file"     # create file in that directory
    chmod a-w "$TARGET_DIR/$file" # remove write-permissions for all
done
