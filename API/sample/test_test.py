import unittest
# This class will be monitored -> displayed to the monitoring dashboard
class test_test_monitoring:

	# These tests will be tested
	def test_I_will_be_tested(self, testcase=None):
		print "testing..."

	def test_so_will_I(self, testcase=None):
		print "testing..."

	# These tests will not be tested
	def I_will_not_be_tested(self):
		print "I won't be tested"

	def neither_will_I(self):
		print "Neither will I"

# This class is used to run unittest (i.e. nosetests)
class test_test_unittest(unittest.TestCase):

	def setUp(self):
		self.alias = test_test_monitoring()

	def test_I_will_be_testd(self):
		self.alias.test_I_will_be_tested(self)

	
