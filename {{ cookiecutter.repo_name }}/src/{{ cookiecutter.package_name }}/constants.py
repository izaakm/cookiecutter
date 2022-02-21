import os

PROJECTDIR = os.path.realpath(os.path.expanduser('~/projects/{{cookiecutter.repo_name}}'))
assert os.path.exists(PROJECTDIR), 'PROJECTDIR does not exist: {}'.format(PROJECTDIR)

DATADIR = os.path.join(PROJECTDIR, 'data')
assert os.path.exists(DATADIR), 'DATADIR does not exist: {}'.format(DATADIR)

# CACHE = os.path.join(PROJECTDIR, '_cache')

# END.
