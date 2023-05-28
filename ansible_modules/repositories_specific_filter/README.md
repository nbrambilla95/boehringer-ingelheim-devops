# Specific Filter - Ansible Module

This is a project featuring an Ansible module I've built. It's designed to filter and list Bitbucket repositories based on various criteria.

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

1. Start off by cloning this repository.
2. Next, place the Python script `repos_specific_filter.py` into your Ansible library directory. By doing so, Ansible will recognize this script as a module.

## Usage

This module can be incorporated within your Ansible playbook as demonstrated below:

```yaml
#Example using specific webhook as a filter
- hosts: localhost
  gather_facts: no

  tasks:
    - name: Using the repos_specific_filter module
      repos_specific_filter:
        project_name: "my_project"
        filter_input: "webhooks"
        key: "url"
        value: "http://my_webhook_url"
        username: "my_username"
        password: "my_password"
```

### Module Parameters

- `project_name` (str, required): Name of the project.
- `filter_input` (str, optional): It can be 'none', 'webhooks', 'permissions/users', 'branches'.
- `key` (str, optional): Field in the JSON obtained.
- `value` (str, optional): Value for the comparison with the field on the JSON (key).
- `username` (str, required): Bitbucket username.
- `password` (str, required): Bitbucket password.

### Return Values

- `output` (str): A list of repositories that match the provided filter.
