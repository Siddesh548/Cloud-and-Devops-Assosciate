*********************** grep *************************
📂 1. journalctl With grep
Command
journalctl | grep --count docker

Output
1573


✔️ Shows total occurrences of the word docker in logs.

Command
journalctl | grep -L docker

Output
(no output)


✔️ -L prints files that DO NOT contain the pattern. Here journalctl produced no file list → so no output.

📄 2. File creation & redirection
Create an empty file
touch redirct.txt

List files
ls


✔️ File appears.

Write to a file (overwrite)
echo "Hello World" > redirect.txt

Append to file
echo "This is telcolearn cloud and devops cohort" >> redirect.txt

View file
cat redirect.txt


✔️ Shows content as expected.

⚠️ 3. sudo apt update Redirected
Command
sudo apt update > redirect.txt

Error Output
Error: Could not get lock /var/lib/apt/lists/lock. It is held by process 32517 (apt)
Error: Unable to lock directory /var/lib/apt/lists/

✅ Reason

Another apt process is running in background.

✅ Solution

Run:

sudo kill -9 32517
sudo rm /var/lib/apt/lists/lock
sudo apt update

🔍 4. Using grep
Count lines containing “cloud”
grep -c cloud redirect.txt

Output
3

Extract only the matched text (occurrences)
grep -o "cloud" redirect.txt | wc -l


✔️ Shows exact number of occurrences.

Show matched file names
grep -l cloud redirct.txt redirect.txt

Word match only (-w)
grep -w cloud redirct.txt redirect.txt

Line number match
grep -n cloud redirect.txt

Inverted match (lines NOT containing cloud)
grep -v cloud redirect.txt

🛠 5. grep Errors & Fixes
❌ Error
grep $s
Usage: grep ...

Reason

Shell expands $s and makes grep think it's wrong syntax.

✔️ Fix

Quote the pattern:

grep '$s' file.txt

❌ Error
grep v cloud redirect.txt
grep: cloud: No such file or directory

Reason

You wrote pattern and file in wrong order.

✔️ Correct:
grep -v cloud redirect.txt


********************** sed ***********************
✂️ 6. sed Commands
Replace 1st occurrence per line
sed "s/cloud/devops/" redirect.txt

Replace all occurrences
sed "s/cloud/devops/g" redirect.txt

Replace 2nd occurrence
sed "s/cloud/devops/2" redirect.txt

Print only replaced lines
sed -n "s/cloud/devops/p" redirect.txt

Delete a specific line
sed '3d' redirect.txt

❌ sed Errors
1️⃣ Error
sed s/cloud/devops redirect.txt
sed: unterminated `s' command


✔️ Missing final /

Fix:

sed "s/cloud/devops/" redirect.txt

2️⃣ Error
sed d$ redirect.txt
sed: extra characters after command


✔️ Wrong syntax.

Fix:

sed '$d' redirect.txt


Deletes last line.

3️⃣ Error
sed d& redirect.txt


✔️ Incorrect usage of &.

🎯 7. Mark Capital Letters using sed
Command
echo "My name is Siddesh" | sed 's/\([A-Z]\)/(\1)/g'

Output
(M)y name is (S)iddesh


****************** awk ***********************
✅ 1. Basic AWK Command Structure
awk 'pattern { action }' file

✅ 2. Print Entire File
awk '{print $0}' pf.csv

✅ 3. Print Specific Columns
awk -F',' '{print $1, $4}' pf.csv


-F',' → tells awk the delimiter is comma.

✅ 4. Filter Rows Based on a Condition
❌ Your incorrect version:
{  $4 > 5000 {print $0} }


This causes:

awk: ^ syntax error

✔ Correct version:
awk -F',' '$4 > 5000 {print $0}' pf.csv

✅ 5. Print Rows Where Salary < 5000
awk -F',' '$4 < 5000' pf.csv

✅ 6. Print Rows Matching a String
awk -F',' '$1 == "A"' pf.csv

✅ 7. Skip Header Line
awk -F',' 'NR>1 {print}' pf.csv

✅ 8. Print Line Numbers
awk '{print NR, $0}' pf.csv

✅ 9. Count Lines Using AWK
awk 'END {print NR}' pf.csv

✅ 10. Find Maximum Salary
awk -F',' 'NR>1 { if($4 > max) max=$4 } END {print max}' pf.csv

🛑 Your actual error explained

You wrote:

{  $4 > 5000 {print $0} }


Issues:

No pattern before {

Missing single quotes

Missing -F',' for CSV

Extra {}

🟢 Correct fixed version
awk -F',' '$4 > 5000 {print $0}' pf.csv


If still no output → check if file has Windows CRLF.

Fix:

dos2unix pf.csv