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

**Variables**
```markdown
## Variables

This playbook uses the following variables:

- `user_roles`: Array of user roles to manage. Example: ['administrator','cms_administrator']
- `project_name`: The name of your Drupal project.
- `branch`: The specific branch of your project.
- `new_admin_username`: The new username for the admin account (random value).
- `new_admin_email`: The new email for the admin account (random value).
- `notify_email`: The email address to send notifications to.

Please note that sensitive data (such as usernames, passwords, and email addresses) should be stored securely, typically in a vault.
