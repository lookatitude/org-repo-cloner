import requests
import os
import subprocess
import shutil
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from colorama import Fore, Style

# Set the GITHUB_TOKEN as your personal access token
GITHUB_TOKEN = ''
ORGANIZATION = ''
CLONE_PATH = ''  # Set this to your desired path or leave it empty to use the current working directory
COMPRESS = True  # Set this to True if you want to compress the repo after cloning

if not CLONE_PATH:
    CLONE_PATH = os.getcwd()

def run_git_clone(repo):
    repo_url = repo['html_url']
    repo_name = repo['name']
    repo_path = os.path.join(CLONE_PATH, repo_name)
    print(f'{Fore.YELLOW}Cloning {repo_url} into {repo_path}...')
    subprocess.run(['git', 'clone', repo_url, repo_path])
    print(f'{Fore.GREEN}Finished cloning {repo_url} into {repo_path}{Style.RESET_ALL}')

    if COMPRESS:
        if shutil.which('tar') is not None:
            print(f'{Fore.YELLOW}Compressing {repo_path} into {repo_path}.tar.gz...')
            subprocess.run(['tar', '-czf', f'{repo_path}.tar.gz', '-C', CLONE_PATH, repo_name])
            print(f'{Fore.GREEN}Finished compressing {repo_path} into {repo_path}.tar.gz{Style.RESET_ALL}')
            shutil.rmtree(repo_path)
        else:
            print(f'{Fore.RED}tar command not found. Skipping compression for {repo_name}{Style.RESET_ALL}')

def get_all_repos(organization):
    page = 1
    repos = []

    # First pass to gather all repo data
    while True:
        url = f"https://api.github.com/orgs/{organization}/repos?per_page=100&page={page}"
        headers = {'Authorization': f'token {GITHUB_TOKEN}'}
        response = requests.get(url, headers=headers)
        data = response.json()

        if not data:
            break

        repos.extend(data)
        page += 1

    print(f'Total repositories to clone: {len(repos)}')

    # Second pass to clone repos
    with ThreadPoolExecutor() as executor:
        list(tqdm(executor.map(run_git_clone, repos), total=len(repos)))

get_all_repos(ORGANIZATION)
