class VcsRepository:
    name = ''
    description = ''
    url = ''
    is_private = False

    def __init__(self, name, description, url, is_private=False):
        """Creates VCS repository instance.

        :param str name: Name (slug)
        :param str description: Description
        :param str url: URL
        :param boolean is_private: Whether this repository is private
        """
        self.name = name
        self.description = description
        self.url = url
        self.is_private = is_private

    def __repr__(self):
        return "{} ({})".format(self.name, 'private' if self.is_private else 'public')
