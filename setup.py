from setuptools import setup

setup(name='orbit',
      version='0.2',
      description='Gives current information about orbital objects of interest',
      url='http://github.com/seanherron/orbit',
      author='Sean Herron',
      author_email='seanherron@gmail.com',
      license='MIT',
      long_description=open('README.txt').read(),
      packages=['orbit'],
      install_requires=[
          'lxml',
          'requests',
          'requests_cache',
          'pyephem',
      ],
      )