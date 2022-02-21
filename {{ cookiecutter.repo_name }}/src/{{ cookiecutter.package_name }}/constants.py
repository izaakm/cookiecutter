import os
import {{cookiecutter.package_name}}

# This assumes that the package has been installed, eg: `pip install -e .`.
# print({{cookiecutter.package_name}}.__file__)  # /abspath/to/{{cookiecutter.repo_name}}/src/{{cookiecutter.package_name}}/__init__.py

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname({{cookiecutter.package_name}}.__file__)))
assert os.path.exists(PROJECT_ROOT), 'PROJECT_ROOT does not exist: {}'.format(PROJECT_ROOT)

DATADIR = os.path.join(PROJECT_ROOT, 'data')
assert os.path.exists(DATADIR), 'DATADIR does not exist: {}'.format(DATADIR)

CACHE = os.path.join(PROJECT_ROOT, '_cache')

# END.
