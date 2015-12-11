from distutils.core import setup

setup(
    name='QualysReporting',
    version='0.2.2',
    install_requires=["requests", "sqlalchemy", "psycopg2"],
    packages=['qgreports', 'qgreports.config', 'qgreports.scripts',
              'qgreports.utils'],
    url='',
    license='',
    author='dmwoods38',
    author_email='',
    description=''
)