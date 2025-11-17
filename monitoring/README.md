# Linux Multi-Terminal Monitoring Activities

This README documents a set of hands-on Linux activities using **three terminals** to monitor system behavior and logs.

## Terminals Overview

* **Terminal 1 (Top Terminal)** → Monitor system processes using `top`
* **Terminal 2 (Activity Terminal)** → Run commands like `tree`, `mkdir`, `touch`, `mv`, `rm`, `rmdir`
* **Terminal 3 (Tail/Journal Terminal)** → View system logs in real time using `sudo journalctl -f`

---

## Terminal 1: Monitoring Processes (`top`)

Command:

```bash
top
```

Sample output when running CPU-intensive commands like `tree`:

```
6633 siddu     20   0    7244   3276   1996 R  96.7   0.1   0:43.97 tree
```

Explanation:

* PID: 6633
* User: siddu
* State: R (Running)
* CPU%: 96.7
* Command: tree

---

## Terminal 2 & 3: Activity Commands and Tail/Journal Logs

### 1️⃣ Create directory `monitoring`

**Activity Terminal:**

```bash
sudo mkdir monitoring
```

**Tail/Journal Terminal:**

```
Nov 17 14:46:11 kali sudo[22553]:    siddu : TTY=pts/0 ; PWD=/home/siddu ; USER=root ; COMMAND=/usr/bin/mkdir monitoring
Nov 17 14:46:11 kali sudo[22553]: pam_unix(sudo:session): session opened for user root(uid=0) by siddu(uid=1000)
Nov 17 14:46:11 kali sudo[22553]: pam_unix(sudo:session): session closed for user root
```

### 2️⃣ Change directory and create files

**Activity Terminal:**

```bash
cd monitoring
sudo touch monitor1 monitor2
```

**Tail/Journal Terminal:**

```
Nov 17 14:46:38 kali sudo[22843]:    siddu : TTY=pts/0 ; PWD=/home/siddu/monitoring ; USER=root ; COMMAND=/usr/bin/touch monitor1
Nov 17 14:46:38 kali sudo[22843]: pam_unix(sudo:session): session opened for user root(uid=0) by siddu(uid=1000)
```

### 3️⃣ Move file to another directory

**Activity Terminal:**

```bash
sudo mv monitoring1/file1 dir3
```

**Tail/Journal Terminal:**

```
Nov 17 15:24:20 kali sudo[41459]:    siddu : TTY=pts/0 ; PWD=/home/siddu ; USER=root ; COMMAND=/usr/bin/mv monitoring1/file1 dir3
Nov 17 15:24:20 kali sudo[41459]: pam_unix(sudo:session): session opened for user root(uid=0) by siddu(uid=1000)
Nov 17 15:24:20 kali sudo[41459]: pam_unix(sudo:session): session closed for user root
```

### 4️⃣ Remove directory recursively

**Activity Terminal:**

```bash
sudo rm -r dir4/KUBERNETES
```

**Tail/Journal Terminal:**

```
Nov 17 15:27:57 kali sudo[43345]:    siddu : TTY=pts/0 ; PWD=/home/siddu ; USER=root ; COMMAND=/usr/bin/rm -r dir4/KUBERNETES
Nov 17 15:27:57 kali sudo[43345]: pam_unix(sudo:session): session opened for user root(uid=0) by siddu(uid=1000)
Nov 17 15:27:57 kali sudo[43345]: pam_unix(sudo:session): session closed for user root
```

### 5️⃣ Remove empty directory

**Activity Terminal:**

```bash
rmdir dir5
```

**Tail/Journal Terminal:**

```
Nov 17 15:28:27 kali sudo[43614]:    siddu : TTY=pts/0 ; PWD=/home/siddu ; USER=root ; COMMAND=/usr/bin/rmdir dir5
Nov 17 15:28:27 kali sudo[43614]: pam_unix(sudo:session): session opened for user root(uid=0) by siddu(uid=1000)
```

### 6️⃣ Attempt to write to root-owned file

**Activity Terminal:**

```bash
echo "Hello Monitoring" > monitor1
```

**Tail/Journal Terminal:**

```
zsh: permission denied: monitor1
```

* Fix with `sudo sh -c 'echo "Hello Monitoring" > monitor1'` or change ownership.

### 7️⃣ Attempt to remove root-owned file

**Activity Terminal:**

```bash
rm monitor1
```

**Tail/Journal Terminal:**

```
rm: cannot remove 'monitor1': Permission denied
```

* Fix with `sudo rm monitor1` or change ownership.

### 8️⃣ Display directory tree

**Activity Terminal:**

```bash
tree /
```

**Tail/Journal Terminal:**

* Typically **no logs** appear for normal users unless a permission error occurs.

---

## Summary

* **Activity Terminal:** Shows command execution output.
* **Top Terminal:** Monitors CPU and memory usage of processes.
* **Tail/Journal Terminal:** Captures system-level logs, sudo commands, and permission errors.
* Each activity is documented with its command and the corresponding Tail/Journal behavior.
