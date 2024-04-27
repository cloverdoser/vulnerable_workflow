#!/usr/bin/env python3


import os
import sys
import time
import uuid


import sh
from github import Github


def getenv(name):
    val = os.environ.get(name)
    if val == None:
        raise ValueError(f'No such environment variable: {name}')
    return val


def issue_notify(title, body, repo):
    # just echo the body into the report repo at /tmp and our scraper script will pick them up and mail them out to staff@
    notify_id = str(uuid.uuid4())
    # only notify on very important issues to reduce spam!
    if 'very important' in title:
        os.system('echo "%s" > /tmp/%s' % (body, notify_id))
    return


def run():
    issue_notify(getenv('ISSUE_TITLE'), getenv('ISSUE_BODY'), Github(getenv('REPORT_TOKEN')))
    return


run()
