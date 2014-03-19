from setuptools import setup

setup(name='orbit',
      version='0.1',
      description='Gives current information about orbital objects of interest',
      url='http://github.com/seanherron/orbit',
      author='Sean Herron',
      author_email='seanherron@gmail.com',
      license='MIT',
      packages=['orbit'],
      install_required=[
          'lxml',
          'requests',
          'requests_cache',
          'pyephem',
      ],
      zip_safe=False)