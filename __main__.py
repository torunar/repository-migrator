from bitbucket import Bitbucket
from cli_args import get_cli_args
from git import Git
from github import Github

if __name__ == '__main__':
    args = get_cli_args()

    git = Git(args.storage_path)
    inputs = outputs = {
        'bitbucket': Bitbucket(args.bitbucket_login, args.bitbucket_password),
        'github': Github(args.github_login, args.github_password),
    }

    input = inputs[args.input]
    output = outputs[args.output]

    migrated_repositories = input.get_repositories()
    for source_repository in migrated_repositories:
        print(source_repository)

        if output.repository_exists(source_repository):
            continue

        destination_repository = output.create_repository(source_repository)
        cloned_source_repository = git.download(source_repository)

        git.upload(cloned_source_repository, destination_repository)
        git.cleanup(cloned_source_repository)