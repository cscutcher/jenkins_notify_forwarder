# -*- coding: utf-8 -*-
"""
Forwards jenkins scm notifications to multiple jenkins instances
"""
from urllib.parse import urljoin
import logging
import sys
import os

from flask import Flask
from flask import request
import requests

DEV_LOGGER = logging.getLogger(__name__)
JENKINS_NOTIFY_URL = 'git/notifyCommit/'
EMPTY_RESPONSE = '''\
No git jobs using repository: {url} and branches: {branches}
No Git consumers using SCM API plugin for: {url}
'''


app = Flask(__name__)

if 'JENKINS_SERVERS' in os.environ:
    app.config['DOWNSTREAM'] = os.environ['JENKINS_SERVERS'].split(',')
elif 'JENKINS_NOTIFY_FORWARDER_SETTINGS' in os.environ:
    app.config.from_envvar('JENKINS_NOTIFY_FORWARDER_SETTINGS')
else:
    app.config['DOWNSTREAM'] = []


@app.route('/' + JENKINS_NOTIFY_URL)
def recieve_git_notification():
    '''
    Receive notification and forward onto downstream servers
    '''
    app.logger.info('Got notification %s', request)

    response_contents = []
    for url in app.config['DOWNSTREAM']:
        app.logger.info('Notifying %s', url)
        try:
            response = requests.get(
                urljoin(url, JENKINS_NOTIFY_URL, allow_fragments=True), params=request.args)
        except (requests.RequestException, ConnectionError) as e:
            app.logger.error('Failed to notify downstream jenkins {!r} : {}'.format(url, e))
        else:
            app.logger.info('Response from %s was %s', response.url, response.content)
            response_contents.append(response.text)

    if response_contents:
        return '\n'.join(response_contents)
    else:
        branches = request.args.get('branches', '')
        url = request.args['url']
        return EMPTY_RESPONSE.format(branches=branches, url=url)


if __name__ == '__main__':
    app.run(*(sys.argv[1:]))
