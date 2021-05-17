import os


class Repository:
    working_dir = ''
    __previous_path = ''

    def __init__(self, working_dir):
        """Creates local repository instance.

        :param str working_dir: Path of the folder where repository files are stored
        """
        self.working_dir = working_dir

    def __enter__(self):
        self.__previous_path = os.getcwd()
        os.chdir(self.working_dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.__previous_path)
