https://github.com/azukauteh/AirBnB_clone_v2/pull/new/test1

#webtack debugging #0

This directory contains tasks and projects related to web stack debugging.

## Description

Web stack debugging involves identifying and fixing issues in web applications or the server configuration. This project focuses on debugging web stack issues and understanding the underlying technologies.

## Installing Docker
```bash
apt-get update
```
Let’s install Docker by installing the docker-io package:
``bash
apt-get -y install docker.io
```
Link and fix paths with the following two commands:
```
ln -sf /usr/bin/docker.io /usr/local/bin/docker
sed -i '$acomplete -F _docker docker' /etc/bash_completion.d/docker.io
```
Finally, and optionally, let’s configure Docker to start when the server boots:
```
update-rc.d docker.io defaults
```
Step 2: Download a Docker Container
Let’s begin using Docker! Download the fedora Docker image:

```
docker pull ubuntu
```
Step 3: Run a Docker Container
Now, to setup a basic ubuntu container with a bash shell, we just run one command. docker run will run a command in a new container, -i attaches stdin and stdout, -t allocates a tty, and we’re using the standard ubuntu container.

```
docker run -i -t ubuntu /bin/bash
```
That’s it! You’re now using a bash shell inside of a ubuntu docker container.

To disconnect, or detach, from the shell without exiting use the escape sequence Ctrl-p + Ctrl-q.

There are many community containers already available, which can be found through a search. In the command below I am searching for the keyword debian:

docker search debian


