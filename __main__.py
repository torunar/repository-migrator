from bitbucket import Bitbucket
from local import Local
from github import Github
from cli_args import get_cli_args
from git import Git

if __name__ == '__main__':
    args = get_cli_args()

    git = Git(args.storage_path)
    inputs = outputs = {
        'bitbucket': Bitbucket(args.bitbucket_login, args.bitbucket_password),
        'github': Github(args.github_login, args.github_password),
        'local': Local(args.storage_path)
    }

    vcs_input = inputs[args.input]
    vcs_output = outputs[args.output]

    migrated_repositories = vcs_input.get_repositories()
    for source_repository in migrated_repositories:
        print(source_repository)

        if vcs_output.repository_exists(source_repository):
            continue

        destination_repository = vcs_output.create_repository(source_repository)
        cloned_source_repository = git.download(source_repository)

        if destination_repository.supports_transfer:
            git.upload(cloned_source_repository, destination_repository)
            git.cleanup(cloned_source_repository)
