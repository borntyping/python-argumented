from distutils.core import setup

setup(
    name             = 'argumented',
    version          = '1.1',
    description      = 'Multiply test cases or functions into several functions with argument sets',
    long_description = open('README.rst').read(),

    author           = 'Sam Clements',
    author_email     = 'sam@borntyping.co.uk',
    url              = 'https://github.com/borntyping/argumented',
    license          = 'MIT License',

    py_modules       = ['argumented'],

    classifiers      = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Testing',
    ],
)