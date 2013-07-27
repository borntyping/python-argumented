==========
argumented
==========

.. image:: https://pypip.in/v/argumented/badge.png
    :target: https://pypi.python.org/pypi/argumented/
    :alt: Latest PyPI version

.. image:: https://api.travis-ci.org/borntyping/python-argumented.png
    :target: https://travis-ci.org/borntyping/python-argumented
    :alt: Travis build status

**argumented** provides a way of 'multiplying' functions - usually test cases - allowing them to be called with multiple argument sets and still appear as separate functions.

It provides several decorators that can be used to add argument sets, and then unpack them.

Decorators
==========

The argument decorators can be used multiple times, or used together - each of them takes the arguments they are given and passes it to ``pack_arguments(func, *args, **kwargs)``, which adds a wrapped function to ``func.__argumented__``.

``@argument(*args, **kwargs)``
------------------------------

Adds the given argument set

``@argument_list(*args)``
-------------------------

Adds each item in args as an argument set

``@argument_tuples(*args)``
---------------------------

Each item in `*args` must be a tuple containing an interable and a mapping, which will then be used as an argument set (i.e. `([], {})`)

``@unpack_arguments``
---------------------

Unpacks all of the argument sets in a class, replacing each function with a list of argument sets with wrapped functions that call each argument set. The wrapped functions are named ``{original name}_{argument set index}``.

Example
=======

In the following example, each test cases would be replaced with two test cases, which would each call the test case with the given arguments.

::

	from unittest import TestCase
	from argumented import *

	@unpack_arguments
	class TestArgumentedCases (TestCase):
			
		@argument("hello", thing="world")
		@argument("goodbye", thing="world")
		def test_greeting (self, greeting, thing):
			self.assertIn(greeting, ["hello", "goodbye"])
			self.assertEquals(thing, "world")
		
		@argument_list(1, 2)
		def test_with_arguments (self, n):
			self.assertIsInstance(n, int)
		
		@argument_tuples( ([1, 2], {'a': 'A'}), ([1, 2], {'a': 'B'}) )
		def test_with_arguments (self, *args, **kwargs):
			self.assertEquals(args, (1, 2))
			self.assertIn(kwargs['a'], ['A', 'B'])

This example can also be found in ``test_argumented.py``.

License
=======

**argumented** is licensed under the MIT License and was originally inspired by `ddt <http://github.com/santtu/ddt>`_.
