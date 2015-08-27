jenkins_notify_forwarder
========================
Stupid simple flask app to forward a git scm notification to multiple downstream jenkins
servers.

Needed to work around limitation of
[Stash Jenkins notification plugin](https://marketplace.atlassian.com/plugins/com.nerdwin15.stash-stash-webhook-jenkins)
that only allows a single jenkins server to specified.

See run.sh for example of how to run
