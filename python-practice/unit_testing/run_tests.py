import unittest

loader = unittest.TestLoader()
suite = loader.discover(".")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)