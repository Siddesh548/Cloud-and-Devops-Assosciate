read -p "Enter your name:" Name

#read -p "Enter your age:" Age

#if [ -z "$Name"  ]; then
#       echo "Username can not be empty"
#fi

#read -p "Enter your age:" Age

#'regx' which checks starts with strings with space also.
if  [[ -z "$Name"|| !"$Name" =~ ^[a-zA-Z\s]*$ ]]; then ## '=~' supports regx
        echo "Name sholud be string"
else
        echo "Name is $Name"
fi

read -p "Enter your age:" Age
if (( Age > 0 && Age < 100 )); then
        echo "The age is $Age"
fi
