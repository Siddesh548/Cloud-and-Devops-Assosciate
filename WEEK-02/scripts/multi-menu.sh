read -p "Enter your chice:" choice

case $choice in
        1) echo "creating file:"
                touch file.txt;;
        2) echo "createing directory"
                mkdir cases;;
        3) echo "listing"
                ls -l;;
        *) echo "Invalid choice";;   
esac
