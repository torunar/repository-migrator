<center>

![](img/logo.png)

# Repository Migrator

Migrates repositories between BitBucket and GitHub.

This tool works in both directions, so you can move your GitHub repositories to BitBucket and vice versa. 

</center>

## Requirements

* Python3.

## How to use

1. Create BitBucket app password with the `Repositories: Read`, `Repositories: Write` and `Repositories: Admin` permissions: 

    https://bitbucket.org/account/settings/app-passwords/new.
3. Create GitHub personal access token with the `repo` scopes:

    https://github.com/settings/tokens/new.
4. Clone repo:
```bash
$ git clone git@github.com:torunar/bitbucket-to-github-migrator.git
```
4. Install dependencies:
```bash
$ cd bitbucket-to-github-migrator
$ pip3 install -r requirements.txt
```
5. To migrate from BitBucket to GitHub, use the following command:
```bash
$ python3 bitbucket-to-github-migrator \
    --input=bitbucket \
    --output=github \
    --bitbucket-login='Your BitBucket username' \ 
    --bitbucket-password='App password from step 1' \
    --github-login='Your GitHub login' \
    --github-password='Personal access token from step 2' 
```
    
6. To migrate from GitHub to BitBucket, use the following command: 
```bash
$ python3 bitbucket-to-github-migrator \
    --input=github \
    --output=bitbucket \
    --bitbucket-login='Your BitBucket username' \ 
    --bitbucket-password='App password from step 1' \
    --github-login='Your GitHub login' \
    --github-password='Personal access token from step 2' 
```