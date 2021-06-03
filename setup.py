from setuptools import setup, find_packages

setup(
      name="mytest",
      version="0.30",
      description="Station Object for AIEXPL PROJECT",
      author="Sica Chang",
      url="http://www.csdn.net",
      license="LGPL",
      packages= find_packages(),
      scripts=["scripts/test.py"],
      )
