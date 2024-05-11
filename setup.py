from distutils.core import setup

# Read the contents of your requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='ai_dojo',
    version=2.0,
    description='',
    author='Christian Staudt',
    url='http://clstaudt.me',
    packages=['ai_dojo'],
    install_requires=requirements,
)
