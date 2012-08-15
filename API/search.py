import inspect, os, sys
# Append the test directory to system's path
sys.path.insert(0, sys.argv[1])
import asserter

def fetch_module():

        # Define all variables needed
        fileList = []
        moduleList = []
        rootdir = sys.argv[1]

        # Find all the files in the test folder
        for root, subFolders, files in os.walk(rootdir):
                for file in files:
                        fileList.append(file)

        # Check if all the tests begin with name test_ and create a module list
        for index in range(len(fileList)):
                if fileList[index].find("test_") != -1:
                        temp = fileList[index].split(".", 2)
                        moduleList.append(temp[0])
	
        # Import all the modules for testing
        module = map(__import__, moduleList)
        return module


# Get the test case from a module
def fetch_class(module):

        for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj):
			if name.find("monitoring") != -1:
                                classToInit = obj(asserter.Asserter('monitoring'))
                                return classToInit, name

# Get all test cases from the test class
def test_methods(classToTest):

        status = True
        for name, obj in inspect.getmembers(classToTest):
                if inspect.ismethod(obj):
                        if name.find("test_") != -1:
                                methodToTest = getattr(classToTest, name)
                                try:
                                        print "testing " + name + "..."
                                        methodToTest()
                                except:
                                        print "Raised exception"
                                        status = False
        return status
