import ConfigParser
from fabric.api import run
from fabric.api import local
from fabric.api import env
from fabric.api import sudo

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

