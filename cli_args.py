import argparse


def get_cli_args():
    """Parses CLI arguments.

    :return: Program arguments passed via CLI
    :rtype Dict
    """
    parser = get_cli_args_parser()

    return parser.parse_args()


def get_cli_args_parser():
    """Gets CLI arguments parser.

    :return: Configured arguments parser

    :rtype ArgumentParser
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i',
        '--input',
        dest='input',
        required=True,
        default='bitbucket',
        choices=['bitbucket', 'github'],
        help='Where repositories are migrated from'
    )
    parser.add_argument(
        '-o',
        '--output',
        dest='output',
        required=True,
        default='github',
        choices=['bitbucket', 'github', 'local'],
        help='Where repositories are migrated to'
    )
    parser.add_argument(
        '-bl',
        '--bitbucket-login',
        dest='bitbucket_login',
        required=False,
        help='Bitbucket: Login'
    )
    parser.add_argument(
        '-bp',
        '--bitbucket-password',
        dest='bitbucket_password',
        required=False,
        help='Bitbucket: App password. Create one on https://bitbucket.org/account/settings/app-passwords/new'
    )
    parser.add_argument(
        '-gl',
        '--github-login',
        dest='github_login',
        required=False,
        help='Github: Login',
    )
    parser.add_argument(
        '-gp',
        '--github-password',
        dest='github_password',
        required=False,
        help='Github: Personal access token. Create one on https://github.com/settings/tokens/new'
    )
    parser.add_argument(
        '-s',
        '--storage-path',
        dest='storage_path',
        required=False,
        default='/tmp/',
        help='Temporary folder to store repositories in'
    )

    return parser
