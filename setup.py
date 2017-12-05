from setuptools import setup

setup(name='git-credential-parameter-store',
      version='0.1',
      description='A git credential helper for AWS parameter store',
      url='http://github.com/tomhillable/git-credential-parameter-store',
      author='Tom Hill',
      author_email='tom@clockworkcubed.com',
      license='MIT',
      packages=['git_credential_parameter_store'],
      scripts=['bin/git-credential-parameter-store'],
      install_requires=['boto3'],
      zip_safe=False)