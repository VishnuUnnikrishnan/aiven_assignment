from setuptools import setup

setup(
   name='PageUp',
   version='0.0.5',
   author='Vishnu Unnikrishnan',
   author_email='vishnu.unni@gmail.com',
   packages=['pageup', 'pageup.tests'],
   scripts=['scripts/web_check.py','scripts/db_upload.py'],
   license='LICENSE',
   description='This application Will check if a web page is up',
   long_description=open('README.md').read(),
   install_requires=[
       "requests",
       "kafka-python",
       "psycopg2-binary",
   ],
)