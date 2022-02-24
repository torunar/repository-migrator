import json

import requests

from vcsrepository import VcsRepository


class Bitbucket:
    base_url = 'https://api.bitbucket.org/2.0/'
    login = ''
    password = ''

    def __init__(self, login, password):
        """Creates BitBucket service instance.

        :param str login: Username
        :param str password: App password
        """
        self.login = login
        self.password = password

    def __request_api(self, endpoint, **kwargs):
        """Requests BitBucket API.

        :param string endpoint: API endpoint
        :return: Request response
        :rtype Any
        """
        response = requests.request(url=self.base_url + endpoint, auth=(self.login, self.password), **kwargs)
        if not response.ok:
            raise Exception('BitBucket API request failed. Check your credentials and network connection')

        return response.json()

    def get_repositories(self):
        """Gets repositories of a user.

        :return:
        :rtype list of VcsRepository
        """
        repositories_raw_data = self.__request_api('repositories?role=owner&pagelen=2048', method='GET')

        repositories = []
        for datum in repositories_raw_data['values']:
            clone_url = None
            for link in datum['links']['clone']:
                if link['name'] == 'ssh':
                    clone_url = link['href']
                    break

            repositories.append(VcsRepository(datum['slug'], datum['description'], clone_url, datum['is_private']))

        return repositories

    def create_repository(self, vcs_repository):
        """Creates repository on GitHub.

        :param VcsRepository vcs_repository: Repository data
        :return: Created repository
        :rtype VcsRepository
        """
        repository_data = {
            'is_private': vcs_repository.is_private,
            'description': vcs_repository.description,
        }

        response = self.__request_api('repositories/{}/{}'.format(self.login, vcs_repository.name),
                                      data=json.dumps(repository_data),
                                      method='POST')

        clone_url = None
        for link in response['links']['clone']:
            if link['name'] == 'ssh':
                clone_url = link['href']
                break

        return VcsRepository(vcs_repository.name,
                             vcs_repository.description,
                             clone_url,
                             vcs_repository.is_private)

    def repository_exists(self, vcs_repository):
        """Checks whether a repository exists

        :param VcsRepository vcs_repository: Repository to check
        :return: Whether repository exists
        :rtype bool
        """
        try:
            self.__request_api('repositories/{}/{}'.format(self.login, vcs_repository.name), method='GET')
            return True
        except:
            pass

        return False
