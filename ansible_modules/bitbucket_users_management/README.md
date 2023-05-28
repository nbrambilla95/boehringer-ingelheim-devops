# Bitbucket User Management - Ansible Module

This project features an Ansible module I've built for managing users and permissions in Bitbucket.

## Table of Contents
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Module Parameters](#module-parameters)
- [Return Values](#return-values)

## Dependencies
To get this Ansible module up and running, you'll need:

- Python 3.x
- Ansible 2.9.x or later
- Python's `requests` library

## Installation
Start off by cloning this repository.
Next, place the Python scripts `bitbucket_user_management.py` and `bitbucket_client.py` into your Ansible library directory. By doing so, Ansible will recognize these scripts as a module.

## Usage
This module can be incorporated within your Ansible playbook as demonstrated below:

```yaml
#Example using specific user management in a Bitbucket repository
- hosts: localhost
  gather_facts: no

  tasks:
    - name: Using the bitbucket_user_management module
      bitbucket_user_management:
        user_email: "email@example.com"
        repository: "some-repo"
        project: "SOME-PROJECT"
        state: "present"
        username: "bitbucket_username"
        password: "bitbucket_password"
        role: "WRITE"
       
