# BitBucket to GitHub repository migrator

## Requirements

* Python3.

## How to use

1. Create BitBucket app password with the `Repositories: Read` permissions: https://bitbucket.org/account/settings/app-passwords/new.
2. Create GitHub personal access token with the `repo` scopes: https://github.com/settings/tokens/new.
3. Clone repo:
```bash
$ git clone git@github.com:torunar/bitbucket-to-github-migrator.git
```
4. Install dependencies:
```bash
$ cd bitbucket-to-github-migrator
$ pip3 install -r requirements.txt
```
5. Run migration process:
```bash
$ python3 bitbucket-to-github-migrator \
    --bitbucket-login='Your BitBucket username' \ 
    --bitbucket-password='App password from step 1' \
    --github-login='Your GitHub login' \
    --github-password='Personal access token from step 2' 
```