for i in 1 2 3 4 5; do
        echo $i
done

#######################

for i in *.sh ; do
        echo $i
done

##########################

for i in $(cat for.sh) ; do
        echo "$i"
done

##########################3

for i in {1..10} ; do
        ping -c 4 127.0.0.$i
done

#############################
