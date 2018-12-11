#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exception.ConnectionError:
        pass


target_url = raw_input("Enter URL here:")

with open("/root/Downloads/paths.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered hidden paths --> " + test_url)
