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
```

## Module Parameters
`user_email` (str, required): Email of the user whose permissions will be changed.

`repository` (str, required): Name of the repository.

`project` (str, required): Name of the project.

`state` (str, required): Desired state for the user, 'present' to add, 'absent' to remove.

`username` (str, required): Bitbucket username.

`password` (str, required): Bitbucket password.

`role` (str, optional): Role to assign to the user. Can be 'REPO_WRITE', 'REPO_READ', 'REPO_ADMIN'. Default is 'REPO_WRITE'.

`url` (str, optional): URL where requests will be made to the Bitbucket API. Default is 'https://bitbucket.com/rest/api/1.0/projects/'.

## Return Values
`message` (str): A message indicating the outcome of the operation.
`changed` (bool): A boolean value indicating whether any changes were made.
