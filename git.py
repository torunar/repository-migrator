import subprocess

from repository import Repository
from vcsrepository import VcsRepository


class Git:
    storage_path = ''

    def __init__(self, storage_path):
        """Creates git service.

        :param str storage_path: Path of the folder to store repositories
        """
        self.storage_path = storage_path.rstrip('/') + '/'

    def download(self, vcs_repository):
        """Downloads repository from VCS.

        :param VcsRepository vcs_repository: Repository to download from VCS
        :return: Local repository instance
        :rtype Repository
        """
        working_dir = self.storage_path + vcs_repository.name
        subprocess.call(['git', 'clone', '--mirror', vcs_repository.url, working_dir])

        return Repository(working_dir)

    @staticmethod
    def upload(repository, vcs_repository):
        """Uploads local repository to VCS.

        :param Repository repository: Local repository to upload
        :param VcsRepository vcs_repository: Remote repository to upload to
        :return: None
        """
        with repository:
            subprocess.call(['git', 'remote', 'add', 'migrator', vcs_repository.url])
            subprocess.call(['git', 'push', '--mirror', 'migrator'])

    @staticmethod
    def cleanup(repository):
        """Removes directory where local repository has been downloaded to.

        :param Repository repository: Local repository
        :return: None
        """
        subprocess.call(['rm', '-rf', repository.working_dir])
