# Cloud-and-Devops-Assosciate

This session is about insatlling the required software for Cloud and Devops.

Git
Docker/Docker-Desktop
Terraform
Ansible
...
while installing the ansible..i got issue...ERROR: Ansible requires the locale encoding to be UTF-8; Detected ISO8859-1.
 ..then I run these cammands--
sudo apt install locales -y
sudo dpkg-reconfigure locales
..in that i select--en_US.UTF-8 (pressing 'spacebar' its selects that language).

--The issue is about language.
en_US.UTF-8

en → English

US → United States

UTF-8 → Unicode text encoding (supports all languages/symbols)