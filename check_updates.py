#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

import requests
from bs4 import BeautifulSoup

def get_versions():
    URL = "https://dlcdn.apache.org/zookeeper/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    versions = []

    links = soup.find_all('a')
    for link in links:
        short_link = link['href'][:-1]
        if 'zookeeper-' in short_link:
            versions.append(short_link[10:])
    return versions

if __name__ == "__main__":
    get_versions()