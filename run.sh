#!/bin/bash
JENKINS_SERVERS='https://ci.jenkins-ci.org/,https://ci.jenkins-ci.org/' python jenkins_notify_forwarder.py 0.0.0.0
