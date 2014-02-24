from fabric.api import *

"""
This is a sample fabfile for a specific server. Customise this fabfile to your settings.
"""

env.hosts = ["user@server:port"]
code_dir = "/path/to/code/root"


def my_server():
    """
    Env parameters for your environment.
    """

    env.hosts = ["user@server:port"]
    env.code_dir = '/var/www/project-template'
    env.config_dir = '/path/to/config/files'
    env.env_dir = "/path/to/virtualenv/environment"
    return