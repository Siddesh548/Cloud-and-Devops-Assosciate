##addition##
add() {
        echo $(($1 + $2))
}
add 5 5


##sub##
sub() {

        subs=$(( $1-$2 ))
        echo "$subs"
}
sub 10 5
