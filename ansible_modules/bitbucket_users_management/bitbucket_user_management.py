#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.bitbucket_client import BitbucketClient

DOCUMENTATION = '''
---
module: bitbucket_management
description:
    - "A module to change permissions on a repository as specific user"
    Parameters:
    user_name:
        description:
            - Change permissions on this user
        required: true
    repository:
        description:
            - Name of the repository
        required: true
    project:
        description:
            - Name of the project
        required: false
    bitbucket_token:
        description:
            - Token for auth on Bitbucket API.
        required: true
    bitbucket_url:
        description:
            - URL where requests will be made
        required: false
'''

EXAMPLES = r'''
- bitbucket_user_management:
    user_email: pepe@example.com
    repository: some-repo
    project: SOME-PROJECT
    state: present
    username: 
    password:
    url: 
    role: WRITE
'''

def run_module():

    module = AnsibleModule(
        argument_spec=dict(
            user_email=dict(type='str', required=True),
            repository=dict(type='str', required=True),
            project=dict(type='str', required=True),
            state=dict(type='str', required=True, choices=[
                'present', 'absent']),
            username=dict(type='str', required=True),
            password=dict(type='str', required=True, no_log=True),
            role=dict(type='str', required=False,
                      default='REPO_WRITE', choices=[
                          'REPO_WRITE', 'REPO_READ', 'REPO_ADMIN']),
            url=dict(type='str', required=False,
                     default=f'https://bitbucket.com/rest/api/1.0/projects/')
        ),
        supports_check_mode=True,

        required_if=[
            ('state', 'present', ['role'])
        ]
    )

    try:
        bitbucket_client = BitbucketClient(
            module.params['url'], module.params['username'], module.params['password'])
        if module.params['state'] == "present":
            response = bitbucket_client.add_permission(
                module.params['project'], module.params['repository'], module.params['user_email'], role=module.params["role"])

        if module.params['state'] == "absent":
            response = bitbucket_client.delete_permission(
                module.params['project'], module.params['repository'], module.params['user_email'])

        module.exit_json(message='success', changed=True)
    except Exception as error:
        module.fail_json(msg=error.args[0])


def main():
    run_module()


if __name__ == '__main__':
    main()
