# 0x0C. Web server

![Author](https://img.shields.io/badge/Author-Azuka%20Uteh-blue.svg)


## Overview
This directory contains the source code and documentation for a web server application. The web server is designed to handle HTTP requests and serve static files and dynamic content.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [Features](#features)
6. [Requirement](#requirement)


## Introduction
The web server is a software application that listens for incoming HTTP requests and responds with the appropriate content based on the request. It can serve static files like HTML, CSS, images, etc., and handle dynamic content generation through server-side programming.

## Installation
To install and run the web server, follow these steps:

1. Clone this repository to your local machine:
```
git clone https://github.com/azukauteh/alx-system_engineering-devops.git
  cd 0x0C-web-server
```

3. Compile the source code using the provided build tools or commands.

4. Run the compiled executable to start the web server.

## Usage

Once the web server is running, you can access it using a web browser or tools like cURL. The server will respond to HTTP requests and serve the appropriate content based on the requested resources.

Example usage:
- Access the server via a web browser: `http://localhost:port`
- Use cURL to make a request: `curl http://localhost:port/path/to/resource`

## Configuration

The web server can be configured using a configuration file or command-line options. Configuration options may include:
- Port number for the server to listen on.
- Document root directory for serving static files.
- Allowed file types/extensions.
- Logging options.
- Security settings.

## Features
- HTTP Server : Listens for incoming HTTP requests and handles them accordingly.
- Static File Serving : Serves static files such as HTML, CSS, JavaScript, images, etc.
- Dynamic Content Generation : Supports server-side programming for generating dynamic content.
- Logging : Provides logging functionality to track server events and requests.
- Error Handling : Properly handles HTTP errors and displays appropriate error pages.

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- You can’t use systemctl for restarting a process
