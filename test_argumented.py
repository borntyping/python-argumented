"""	A set of example tests for `argumented` """

from unittest import TestCase, TestLoader, TextTestRunner, main

from argumented import *

@unpack_arguments
class TestArgumentedCases(TestCase):
		
	@argument("hello", thing="world")
	@argument("goodbye", thing="world")
	def test_greeting(self, greeting, thing):
		self.assertTrue(greeting in ["hello", "goodbye"])
		self.assertEqual(thing, "world")
	
	@argument_list(1, 2)
	def test_with_argument_list (self, n):
		self.assertTrue(isinstance(n, int))

	@argument_tuples(([1, 2], {'a': 'A'}), ([1, 2], {'a': 'B'}))
	def test_with_argument_tuples(self, *args, **kwargs):
		self.assertEqual(args, (1, 2))
		self.assertTrue(kwargs['a'] in ['A', 'B'])

if __name__ == '__main__':
    main()
