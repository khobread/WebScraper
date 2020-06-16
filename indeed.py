#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:01:01 2020

@author: haydenlee
"""
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=Consultant&l&limit=50&radius=10&ts=1590087527830&rq=1&rsIdx=0&fromage=last&newcount=121544={LIMIT}"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    
    pagination = soup.find("div", {"class": "s-pagination"})
    links = pagination.find_all("a")
        
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
            
    max_page = pages[-1]
    return max_page



def extract_job(html):
    title = html.find("div", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company:
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
    else:
        company = None
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html("data-jk")
    return {
        'Title': title,
        'Company': company,
        'Location': location,
        "link": f"https://www.indeed.com/viewjob?jk={job_id}"
    }



def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scraping page {page}...")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs