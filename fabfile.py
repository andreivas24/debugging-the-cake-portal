# pylint: disable-msg=W0401,W0614
"""
Deployment automation.
"""
from rdcore.deployment.automation import *

# Project description
env.project_name = 'debugging_cake_portal'
# env.svn_url_template = 'https://serv-sources.jouve-hdi.com/jouve/bpo_geodis/{project_name}'
env.git_url_template = 'https://git.jouve-hdi.com/CVAR/debugging_cake_portal.git'
# env.project_dir_template = '/home/projet/{project_name}/{project_name}'
env.project_dir_template = "/projet/apps/{project_name}"
# Build variables
env.build_python_version = "3.8"
env.build_variant = "focal"
env.build_host = "localhost"

env.roledefs['staging'] = []
env.roledefs['prod'] = []
env.roledefs['int'] = []
env.upload_with_setuptools = True
compute_roledefs()


def get_install_options():
    """Get install.py options.

    Set option --use-previous-answers if the Fabric env var
    all-install-questions is not set.
    """
    install_options = '--compare-process '
    if not env.get('all-install-questions'):
        install_options += '--use-previous-answers '
    return install_options


# Override the default install.get_install_options function
install.get_install_options = get_install_options