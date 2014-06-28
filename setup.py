from setuptools import setup

setup(
    name='edx-saml-auth',
    version='0.1',
    description='SAML third party authentication provider for edX',
    packages=['samlauth',],
    install_requires=['python-social-auth',]
)
