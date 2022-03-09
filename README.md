<p align="center">
    <img src="https://raw.githubusercontent.com/torunar/repository-migrator/master/img/logo.png" alt="Logo" />
</p>

# Repository Migrator

Migrates repositories between BitBucket, GitHub, and local storage.

This tool works in both directions, so you can move your GitHub repositories to BitBucket and vice versa.

You can also back up your repositories locally. 

## Requirements

* Python3.

## Installation

1. _(If you plan to use BitBucket)_ Create BitBucket app password with the `Repositories: Read`, `Repositories: Write` and `Repositories: Admin` permissions: 

    https://bitbucket.org/account/settings/app-passwords/new.
3. _(If you plan to use GitHub)_ Create GitHub personal access token with the `repo` scopes:

    https://github.com/settings/tokens/new.
4. Clone the tool repo:
```bash
$ git clone git@github.com:torunar/repository-migrator.git
```
4. Install dependencies:
```bash
$ cd repository-migrator
$ pip3 install -r requirements.txt
```

## Usage

### Migrate from BitBucket to GitHub
```bash
$ python3 repository-migrator \
    --input=bitbucket \
    --output=github \
    --bitbucket-login='Your BitBucket username' \ 
    --bitbucket-password='App password from Installation step 1' \
    --github-login='Your GitHub login' \
    --github-password='Personal access token from Installation step 2' 
```
    
### Migrate from GitHub to BitBucket 
```bash
$ python3 repository-migrator \
    --input=github \
    --output=bitbucket \
    --bitbucket-login='Your BitBucket username' \ 
    --bitbucket-password='App password from Installation step 1' \
    --github-login='Your GitHub login' \
    --github-password='Personal access token from Installation step 2' 
```

### Back up repositories from GitHub
```bash
$ python3 repository-migrator \
    --input=github \
    --output=local \
    --github-login='Your GitHub login' \
    --github-password='Personal access token from Installation step 2' 
```

### Back up repositories from BitBucket 
```bash
$ python3 repository-migrator \
    --input=bitbucket \
    --output=local \
    --bitbucket-login='Your BitBucket username' \ 
    --bitbucket-password='App password from Installation step 1'  
```
