import os

from vcsrepository import VcsRepository


class Local:
    storage_path = ''

    def __init__(self, storage_path):
        """Creates Local service instance.

        :param str tmp_path: Path to store local repositories
        """
        self.storage_path = storage_path.rstrip('/') + '/'

    def create_repository(self, vcs_repository):
        """Creates repository locally.

        :param VcsRepository vcs_repository: Repository data
        :return: Created repository
        :rtype VcsRepository
        """

        return VcsRepository(vcs_repository.name,
                             '',
                             self.storage_path + '/' + vcs_repository.name,
                             False,
                             False)

    def repository_exists(self, vcs_repository):
        """Checks whether a repository exists

        :param VcsRepository vcs_repository: Repository to check
        :return: Whether repository exists
        :rtype bool
        """

        return os.path.exists(self.storage_path + vcs_repository.name)
