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
        result = response.json()
        if 'errors' in result:
            raise Exception('GitHub API request failed: {}'.format(result['message']))
        if not response.ok:
            raise Exception('GitHub API request failed. Check your credentials and network connection')

        return result

    def create_repository(self, vcs_repository):
        """Creates repository on GitHub.

        :param VcsRepository vcs_repository: Repository data
        :return: Created repository
        :rtype VcsRepository
        """
        repository_data = {
            'name': vcs_repository.name,
            'description': self.__normalize_description(vcs_repository.description),
            'private': vcs_repository.is_private
        }
        response = self.__request_api('user/repos', data=json.dumps(repository_data), method='POST')

        return VcsRepository(vcs_repository.name,
                             vcs_repository.description,
                             response['ssh_url'],
                             vcs_repository.is_private)

    def repository_exists(self, vcs_repository):
        """Checks whether a repository exists

        :param VcsRepository vcs_repository: Repository to check
        :return: Whether repository exists
        :rtype bool
        """
        try:
            self.__request_api('repos/{}/{}'.format(self.login, vcs_repository.name), method='GET')
            return True
        except:
            pass

        return False

    @staticmethod
    def __normalize_description(description):
        """Removes control characters from repository description.

        :param string description:
        :return: Normalized description
        :rtype string
        """
        return ' '.join(description.split())
