#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:22:59 2020

@author: haydenlee
"""
import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=consultant"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    print(pages)

def get_jobs():
    last_page = get_last_page()
    return []