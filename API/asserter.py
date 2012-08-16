"""""""
@Author:        Max Hsieh
@Date:          08/16/2012
"""""""

# This class supports two different testing environments: unittest and monitoring
class Asserter:
        env = 'unittest'
        def __init__(self, env):
                self.env = env

        def assertEqual(self, caller, value, expected):
                if self.env == 'unittest':
                        caller.assertEqual(value, expected)
                elif self.env == 'monitoring':
                        if value != expected:
                                raise Exception('Monitoring failed')

	def assertNotEqual(self, caller, value, expected):
		if self.env == 'unittest':
			caller.assertNotEqual(value, expected)
		elif self.env == 'monitoring':
			if value == expected:
				raise Exception('Monitoring falied')
