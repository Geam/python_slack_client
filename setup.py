from setuptools import setup

setup (name = 'python_slack_client',
    packages = ['python_slack_client'],
    version = '0.0.1',
    author = 'marc delage',
    author_email = 'mdelage@student.42.fr',
    url = 'https://github.com/Geam/python_slack_client',
    description = 'Slack client for terminal write in python',
    licence = 'MIT',
    install_requires = ['slacksocket >= 0.7']
)
