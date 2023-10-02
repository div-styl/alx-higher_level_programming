#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""

import sys
import requests

def get_recent_commits(owner, repo, limit=10):
    """ retrieve recent commit """
    url = f'https://api.github.com/repos/{owner}/{repo}/commits?per_page={limit}'
    response = requests.get(url)
    return response.json()

def print_commits(commits):
    """ print commits """
    for commit in commits:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print(f'{sha}: {author_name}')

def main():
    """ the functions
    """
    owner = sys.argv[1]
    repo = sys.argv[2]

    recent_commits = get_recent_commits(owner, repo)
    print_commits(recent_commits)

if __name__ == "__main__":
    main()
