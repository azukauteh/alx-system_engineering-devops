# 0x0A Configuration Management

![Author](https://img.shields.io/badge/Author-Azuka%20Uteh-blue.svg)


## Table of Contents
1. [Introduction](#1-introduction)
2. [Purpose](#2-purpose)
3. [Installation and Setup](#3-installation-and-setup)
4. [Requirements](#4-requirements)

## 1. Introduction

Welcome to the 0x0A Configuration Management project! This directory is focused on configuration management, providing a structured approach to manage configurations for various applications and services.

## 2. Purpose

The purpose of this project is to streamline the management of configurations for software applications and services. Configuration management is critical for maintaining consistency, reducing errors, and ensuring the seamless deployment and operation of applications across different environments.

## 3. Installation and Setup

- Install puppet
```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
- Install puppet-lint
```
$ gem install puppet-lint
```


## 4. Requirements

# General

- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension .pp
