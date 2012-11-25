"""	A set of example tests for `argumented` """

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
