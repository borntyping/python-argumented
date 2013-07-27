from setuptools import setup

setup(
    name             = 'argumented',
    version          = '1.1.0',
    description      = 'Multiply test cases or functions into several functions with argument sets',
    long_description = open('README.rst').read(),

    author           = 'Sam Clements',
    author_email     = 'sam@borntyping.co.uk',
    url              = 'https://github.com/borntyping/python-argumented',
    license          = 'MIT License',

    py_modules       = ['argumented'],

    classifiers      = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
    ],
)
