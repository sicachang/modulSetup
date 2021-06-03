from setuptools import setup, find_packages

setup(
      name="mytest",
      version="0.30",
      description="My test module",
      author="Sica Chang",
      url="http://www.csdn.net",
      license="LGPL",
      packages= find_packages(),
      scripts=["scripts/test.py"],
      )
