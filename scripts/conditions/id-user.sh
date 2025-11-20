if [ "$UID" -eq 0 ]; then
echo "ROOT USER"
else
echo "REGULAR USER"
fi
