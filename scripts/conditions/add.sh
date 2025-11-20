read -p "Enter n1:" n1
read -p "ENter n2:" n2

if [ "$n1" -eq "$n2" ]; then
        echo "YES"
else
        echo "NO"
fi

##############################

c=$((n1+n2))
echo "the sum is:$c"

##########################################

read -p "filename": file

if [ -e "$file" ]; then
        echo "yes"
else 
        echo "no"
fi

#######################################

read -p "Enter the file to check:" file

if [ -x "$file" ]; then
        echo "It has permission to execute"
elif [ -r "$file" ]; then
        echo "It has read permission"
else
        echo "It has write ermission"
fi
