🖥️ Terminal 1: Run Python Logging Script

## Command
python3 systd.py --rate 1

ouput:

Using SysLogHandler to /dev/log or UDP.
2025-11-18 17:14:43,514 INFO User login succeeded (seq=1, time=2025-11-18 17:14:43, host=kali)
2025-11-18 17:14:44,548 INFO User login failed: invalid password (seq=2, time=2025-11-18 17:14:44, host=kali)
2025-11-18 17:14:45,552 INFO Background job completed (seq=3, time=2025-11-18 17:14:45, host=kali)


🖥️ Terminal 2: View System Logs Using journalctl

## Command
journalctl | grep Nov

Output:

Nov 18 17:14:43 kali python3[65587]: 2025-11-18T17:14:43 pylogtest[65587]: INFO: User login succeeded (seq=1, time=2025-11-18 17:14:43, host=kali)
Nov 18 17:14:44 kali python3[65587]: 2025-11-18T17:14:44 pylogtest[65587]: INFO: User login failed: invalid password (seq=2, time=2025-11-18 17:14:44, host=kali)
Nov 18 17:14:45 kali python3[65587]: 2025-11-18T17:14:45 pylogtest[65587]: INFO: Background job completed (seq=3, time=2025-11-18 17:14:45, host=kali)


🐳 Terminal 1: Run Logging Script Inside Docker Container

## Command
sudo docker run stress1

Output:

Using SysLogHandler to /dev/log or UDP.
2025-11-18 13:00:26,370 INFO User login succeeded (seq=1, time=2025-11-18 13:00:26, host=558df6ba140d)
2025-11-18 13:00:27,381 INFO User login failed: invalid password (seq=2, time=2025-11-18 13:00:27, host=558df6ba140d)
2025-11-18 13:00:28,384 INFO Background job completed (seq=3, time=2025-11-18 13:00:28, host=558df6ba140d)
2025-11-18 13:00:29,389 INFO Periodic health check OK (seq=4, time=2025-11-18 13:00:29, host=558df6ba140d)
2025-11-18 13:00:30,391 INFO Disk usage threshold crossed (seq=5, time=2025-11-18 13:00:30, host=558df6ba140d)

🖥️ Terminal 2: Check Docker-Related Logs in journalctl

## Command
journalctl | grep docker

Output:

Nov 18 18:30:24 kali systemd[1]: Started docker-558df6ba140d154259309863ee0f033aaf67b5877b9d844ed7aea6dbb2c16efe.scope - libcontainer container 558df6ba140d154259309863ee0f033aaf67b5877b9d844ed7aea6dbb2c16efe.
Nov 18 18:30:24 kali kernel: docker0: port 1(vethcf01d69) entered blocking state
Nov 18 18:30:24 kali kernel: docker0: port 1(vethcf01d69) entered disabled state
Nov 18 18:30:25 kali kernel: docker0: port 1(vethcf01d69) entered blocking state
Nov 18 18:30:25 kali kernel: docker0: port 1(vethcf01d69) entered forwarding state
Nov 18 18:30:25 kali NetworkManager[694]: <info>  [1763470825.1200] device (docker0): carrier: link connected