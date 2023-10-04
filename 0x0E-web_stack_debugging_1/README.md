# 0x0E. Web Stack Debugging #1

This directory contains solutions and explanations for the Web Stack Debugging project, which is part of the alx_Africa software engineering School curriculum. The project focuses on debugging a web application and understanding the various components of the web stack.

## Project Description

In this project, we are tasked with debugging a faulty web application. The application is built using a specific web stack, and our goal is to identify and fix any issues to make it functional.

## Files

- ` 0-nginx_likes_port_80`: Nginx installation from listening on port 80.
- `1-debugging_made_short`: Make it sweet and short.

## File Descriptions

1.  0-nginx_likes_port_80
   - This script is designed to fix a web server and ensure that it returns a page. It involves diagnosing and rectifying issues that prevent the web server from functioning correctly.

2. 1-debugging_made_short
   - This script aims to fix a web server and enable the transfer of a specified file from the server to the client. Similar to the first script, it involves debugging and resolving issues in the web server configuration.

## Usage

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/azukauteh/alx-system_engineering-devops.git
   ```

2. Navigate to the project directory.
   ```bash
   cd 0x0E-web_stack_debugging_1
   ```

3. Run the scripts with appropriate permissions.
   ```
   root@966c5664b21f:/# curl 0:80
   curl: (7) Failed to connect to 0 port 80: Connection refused
   root@966c5664b21f:/# ./0-nginx_likes_port_80 > /dev/null 2&1
   root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
   ```
- 1-debugging_made_short

```
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# cat -e 1-debugging_made_short | wc -l
5
root@966c5664b21f:/# ./1-debugging_made_short
root@966c5664b21f:/# curl 0:80
```
