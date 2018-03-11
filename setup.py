from setuptools import setup

setup(name = 'health_fhir',
        version = '1.0.0',
        description = 'Provides FHIR interface to GNU Health.',
        url = 'https://github.com/teffalump/health_fhir',
        author = 'teffalump',
        author_email = 'chris@teffalump.com',
        packages = ['health_fhir'],
        install_requires = ['fhirclient'],
        zip_safe = False,
        classifiers = ['Development Status :: 2 - Pre-Alpha',
                       'Programming Language :: Python',
                       'Programming Language :: Python :: 3',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                       'Operating System :: OS Independent'])