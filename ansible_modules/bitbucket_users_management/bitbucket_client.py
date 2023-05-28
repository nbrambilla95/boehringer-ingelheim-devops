#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


class BitbucketClient:

    def __init__(self, bitbucket_url, bitbucket_user, bitbucket_password):
        self._bitbucket_url = bitbucket_url
        self._bitbucket_user = bitbucket_user
        self._bitbucket_password = bitbucket_password

        self._query_headers = {
            "Content-Type": "application/json"
        }
        self._auth = (bitbucket_user, bitbucket_password)

    """
    Generate the request to Bitbucket API

    Raises:
        Exception: Connectivity issues with Bitbucket API

    Returns:
        dict: Response from Bitbucket API
    """

    def _make_request(self, uri, body={}, method="GET"):
        try:
            response = requests.request(method,
                                        url=f"{self._bitbucket_url}{uri}",
                                        data=body,
                                        headers=self._query_headers,
                                        auth=self._auth
                                        )

            return response
        except requests.ConnectionError:
            raise Exception(
                "Network Error: Cant connect to " + self._bitbucket_url)

    """
    Remove user from Bitbucket repository

    Raises:
        Exception: API cannot handle the request

    Returns:
        dict: Response from Bitbucket API
    """

    def delete_permission(self, project_name, repository, user_email) -> dict:
        uri = f"{project_name}/repos/{repository}/permissions/users?name={user_email}"
        response = self._make_request(uri, method="DELETE")

        if response.status_code != 204:
            raise Exception(
                f"ErrorCode: {response.status_code}. Msg: " + response.json()["errors"][0]["message"])
        else:
            return response

    """
    Add a user to a Bitbucket repository
    
    Raises:
        Exception: API cannot handle the request

    Returns:
        dict: Response from Bitbucket API
    """

    def add_permission(self, project_name, repository, user_email, role="REPO_WRITE") -> dict:
        uri = f"{project_name}/repos/{repository}/permissions/users?name={user_email}&permission={role}"
        response = self._make_request(uri, method="PUT")
        
        if response.status_code != 204:
            raise Exception(
                f"ErrorCode: {response.status_code}. Msg:" + response.json()["errors"][0]["message"])
        else:
            return response

    """
    Get a specific user from Bitbucket
    Raises:
        Exception: API cannot handle the request

    Returns:
        dict: Response from Bitbucket API with user information
    """

    def get_user(self, project_name, repository, user_email) -> dict:

        uri = f"{project_name}/repos/{repository}/permissions/users?filter={user_email}"
        response = self._make_request(uri)
        if response.status_code != 200 and response.json()["size"] != 1:
            raise Exception(
                f"ErrorCode: {response.status_code}. Msg: " + response.json())
        else:
            return response.json()["values"][0]["user"]
