# -*- coding: utf-8 -*-
"""
Forwards jenkins scm notifications to multiple jenkins instances
"""
import logging
import sys
from flask import Flask

DEV_LOGGER = logging.getLogger(__name__)


app = Flask(__name__)

@app.route('/git/notifyCommit')
def recieve_git_notification(request):
    '''
    Receive notification and forward onto downstream servers
    '''


if __name__ == '__main__':
    app.run(*(sys.argv[1:]))
