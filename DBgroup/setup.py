from setuptools import setup
#comment
setup(name="dublinbikes",
      version="0.1",
      description="Assignment 4 Project",
      url="",
      author="Daniel Cummins",
      author_email="daniel.cummins@ucdconnect.ie",
      license="GPL3",
      packages=['src'],
      entry_points={
          'console_scripts':['dublinbikes=src.main:populate'] 
                })