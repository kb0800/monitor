from search import *
from updateDB import *
import os, sys, time

# Main daemon loop
def main():
	
	while True:
	
		# Get the class module and name to test, then test the module
		# For each module, get the test class; for each test class, get the 
		# corresponding test methods
		moduleToTest = fetch_module()

		for module in moduleToTest:
			# Get the required info for updating to DB
			classToTest, class_name = fetch_class(module)
			words = class_name.split("_", 2)
			status = test_methods(classToTest)
			category = words[0]

			#Update to DB
			setupDB(status, category, class_name)

		# Remove all .pyc files and run tests again after 10 sec
		command = "rm *.pyc"
		os.system(command)		

		print "Finished testing, will now halt for 10 sec..."
		time.sleep(10)

if __name__ == "__main__":
	main()











