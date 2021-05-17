import json
import requests

from vcsrepository import VcsRepository


class Github:
    base_url = 'https://api.github.com/'
    login = ''
    password = ''

    def __init__(self, login, password):
        """Creates GitHub service instance.

        :param str login: Username
        :param str password: Personal access token
        """
        self.login = login
        self.password = password

    def __request_api(self, endpoint, **kwargs):
        """Requests GitHub API.

        :param str endpoint: API endpoint
        :return: Request response
        :rtype Any
        """
        response = requests.request(url=self.base_url + endpoint,
                                    auth=(self.login, self.password),
                                    headers={'Accept': 'application/vnd.github.v3+json'},
                                    **kwargs)

        return response.json()

    def create_repository(self, vcs_repository):
        """Creates repository on GitHub.

        :param VcsRepository vcs_repository: Repository data
        :return: Created repository
        :rtype VcsRepository
        """
        repository_data = {
            'name': vcs_repository.name,
            'description': vcs_repository.description,
            'private': vcs_repository.is_private
        }
        response = self.__request_api('user/repos', data=json.dumps(repository_data), method='POST')

        return VcsRepository(vcs_repository.name,
                             vcs_repository.description,
                             response['ssh_url'],
                             vcs_repository.is_private)
