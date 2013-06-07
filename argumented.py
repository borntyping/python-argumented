"""
Pack and unpack functions into a set of wrapped functions with set arguments
"""

__all__ = ['unpack_arguments', 'argument', 'argument_list', 'argument_tuples']

from functools import wraps

def unpack_arguments(cls):
	"""
	Unpacks any function in the class that has a list of argumented functions
	
	The argumented functions are set as attributes on the class,
	and the original function is removed from the class
	"""
	for name, attr in cls.__dict__.items():
		if callable(attr) and hasattr(attr, '__argumented__'):
			for i, func in enumerate(attr.__argumented__):
				setattr(cls, name + "_" + str(i), func)
			delattr(cls, name)
	return cls

def pack_arguments(func, *args, **kwargs):
	"""
	Packs a wrapper around `func` into `func.__argumented__`
	
	The wrapper calls `func` with the given arguments, and will be moved into
	the main namespace when `@unpack_arguments` is called on the class
	containing the function.
	"""
	
	# Ensure the list of argumented functions exists
	if not hasattr(func, '__argumented__'):
		func.__argumented__ = []
	
	# Create a wrapper for the function, using the given arguments
	@wraps(func)
	def argumented_function (self):
		return func(self, *args, **kwargs)
		
	# Add the function to the argumented list
	func.__argumented__.append(argumented_function)
	
	return func

def argument(*args, **kwargs):
	"""	Calls `pack_arguments` with the given arguments """
	return lambda f: pack_arguments(f, *args, **kwargs) and f
	
def argument_list(*args):
	"""	Calls `pack_arguments` with each given argument """
	return lambda f: [pack_arguments(f, a) for a in args] and f

def argument_tuples(*args):
	"""	Calls `pack_arguments` with each given argument list """
	return lambda f: [pack_arguments(f, *a, **b) for (a, b) in args] and f
