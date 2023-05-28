# Ansible Playbook for Drupal User Management

This is an Ansible playbook for managing Drupal users and roles. It performs various tasks such as querying for users with specific roles, blocking those users, and updating the administrator's username, password, and email.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Variables](#variables)
- [Tasks](#tasks)

## Dependencies

To get this Ansible playbook up and running, you'll need:

- Ansible 2.9.x or later
- Access to a Drupal instance

## Installation

1. Clone this repository.
2. Replace the necessary variables within the playbook with your specific configurations.

## Usage

This playbook is meant to be run with Ansible. You can use the following command to run the playbook:

```bash
ansible-playbook playbook.yml -i hosts
```
