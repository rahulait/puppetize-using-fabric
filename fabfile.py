#############################################################################
# File: fabfile.py
# Author: Rahul Sharma <rahuls@ccs.neu.edu>
# Desc: automates task of performing common tasks on
#       all the nodes selected. Tasks can be done in
#       parallel or sequentially.
#
# Target Versions: Python2
#
# Dependencies
# -----------------
# RHEL based:
# yum install fabric
#
# Debian based:
# sudo apt-get install fabric
#
# Both:
# sudo pip install fabric
#############################################################################

import ConfigParser
from fabric.api import run
from fabric.api import local
from fabric.api import env
from fabric.api import sudo
from fabric.context_managers import prefix

CONFIG_FILE = "settings.ini"

config = ConfigParser.ConfigParser()
config.read(CONFIG_FILE)

env.hosts = config.get('env', 'hosts').split()
env.password = config.get('env', 'password')
env.warn_only = config.getboolean('env', 'warn_only')


def test():
    '''
    Run tempest and make sure there are no failures.
    '''
    local("some code to run tempest run")


def commit():
    local("git add -p && and git commit")


def push():
    local("git push")


def get_logs():
    run(sudo("tail -f <respective_file>", shell=False))


def puppetize():
    run(sudo("puppet agent -t", shell=False))


def yum_update():
    if not(registered()):
        register_node()
    run(sudo("yum update -y", shell=False))


def restart_services():
    run(sudo("openstack-service restart", shell=False))


def register_node():
    user = config.get('redhat', 'user')
    password = config.get('redhat', 'password')
    command = "subscription-manager register --user=%s --password=%s" \
              % (user, password)
    run(sudo(command, shell=False))

    pool = config.get('redhat', 'pool')
    command = "subscription-manager attach --pool=%s" % pool
    run(sudo(command, shell=False))


def registered():
    #run(sudo(, shell=False))
    pass


def get_vm_tap_interface():
    with prefix(". /home/rahuls/keystonerc_admin"):
        run("neutron net-list", shell=False)

