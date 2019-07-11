import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'readme.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ip2location-timezone',
    version='1.0.0',
    packages=['ip2location_timezone'],
    include_package_data=True,
    license='MIT License',
    description='Django IP2Location Timezone is a simple Django package that can help you easily display your website visitor the time according to their location.',
    long_description=README,
    url='https://github.com/ip2location/django-ip2location-timezone',
    author='IP2Location',
    author_email='support@ip2location.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)