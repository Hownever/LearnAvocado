from setuptools import setup, find_packages


setup(name='avocado-framework-plugin-helloworld',
      description='Avocado Plugin for Execution of HttpRunner Framework tests',
      version=open("VERSION", "r").read().strip(),
      author='js(jiashuo)',
      author_email='jiashuo1@jd.com',
      url='http://www.jdcloud.com/',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['hello'],
      entry_points={
          'avocado.plugins.cli': [
              'hello = mypluginpack.hello:HelloWorld',
          ]}
      )
