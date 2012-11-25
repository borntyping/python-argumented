from distutils.core import setup
from argumented import __version__, __doc__

setup(
    name             = 'argumented',
    version          = __version__,
    description      = __doc__,
    long_description = open("README.md").read(),

    author           = 'Sam Clements',
    author_email     = 'sam@borntyping.co.uk',
    url              = 'https://github.com/borntyping/argumented',
    license          = 'MIT License',

    packages         = ['argumented'],

    classifiers      = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Testing'
    ],
)