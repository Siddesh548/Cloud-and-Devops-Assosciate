read -p "Do you need system stats:" choice
case $choice in
        Yes) echo "Th stats are ready"
            lscpu && free -h && df -h ;;
        No) echo "Exit";;
        *) echo "Invalod choice";;
esac
