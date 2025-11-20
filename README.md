# Cloud-and-Devops-Assosciate

This document contains the steps I followed while installing the required software for my Cloud and DevOps setup.

The tools installed in this session are:

Git

Docker / Docker Desktop

Terraform

Ansible

Minikube

Kubectl

Other supporting utilities

1. Ansible Installation Issue (Locale Error)
2.  Error Encountered

ERROR: Ansible requires the locale encoding to be UTF-8; Detected ISO8859-1.

**Reason**:

My system locale was not set to UTF-8, which is required by Ansible.

**Solution**:

I installed and reconfigured the locale settings:

sudo apt install locales -y
sudo dpkg-reconfigure locales


During the configuration, I selected:

en_US.UTF-8 (using the spacebar to select)

**Meaning**:

en → English

US → United States

UTF-8 → Unicode text encoding that supports all languages and symbols

After enabling en_US.UTF-8, the Ansible installation worked correctly.

2. Minikube Using Podman Instead of Docker
**Problem**:

When starting Minikube, it was selecting Podman instead of Docker as the container runtime.

**Reason**:

The environment settings were pointing to Podman, so Minikube detected Podman first.

**Solution**:

I forced Minikube to use Docker by setting the Docker socket manually:

export DOCKER_HOST=unix:///var/run/docker.sock


Then I explicitly started Minikube using the Docker driver:

minikube start --driver=docker


This ensured Minikube used Docker instead of Podman.
