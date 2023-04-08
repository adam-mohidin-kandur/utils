#!/usr/bin/env python3
import time
import argparse

import utils
from client import Client


argument_parser = argparse.ArgumentParser(description="in dev")
argument_parser.add_argument("login", type=str)
argument_parser.add_argument("password", type=str)
argument_parser.add_argument("job_name", type=str)
args = argument_parser.parse_args()

login = args.login
password = args.password
job_name = args.job_name

client = Client()

client.first_page.click_login()
client.login_page.login(login, password)
client.main_page.search(job_name)
client.jobs_page.check_moscow_checkbox()

for i in range(6):
    jobs = client.jobs_page.find_jobs()
    for job in jobs:
        utils.apply_jobs(client, job, login, password)
    client.jobs_page.click_page(i + 1 + 1)
