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
