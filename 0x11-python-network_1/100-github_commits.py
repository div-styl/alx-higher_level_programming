#!/usr/bin/python3
""" module doc """
from sys import argv
import requests


def main():
    """
    Main which takes 2 arguments:
    owner, repo, limit
    """
    owner = argv[1]
    repo = argv[2]
    limit = 10
    url = f'https://api.github.com/repos\
/{repo}/{owner}/commits?per_page={limit}'

    response = requests.get(url).json()
    for commit in response:
        name = commit.get("commit").get("author").get("name")
        print(f'{commit.get("sha")}: {name}')


if __name__ == "__main__":
    main()
