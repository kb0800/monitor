Introduction
-------------

This open source project monitors your own defined test cases (wheteher it's for website API monitoring or selenium integration test). The daemon searches for the test cases in an exact pattern, so make sure you read this file before running the daemon.

IMPORTANT !!!
-------------

Make sure you name your test cases as the following:
+ For file names: name the file that start with *test_*
        (i.e. `test_me.py`)
+ For class names: name the class that ends with *monitoring*
        (i.e. `class restaurant_info_monitoring`)
+ For method names: name the methods inside the class that start with *test_*
        (i.e. `test_restaurant_info)`
+ Refer to the **How the daemon works** section for why naming is important
+ See the sample/ directory for naming examples

Logistic / Background
---------------------

I build this daemon to monitor a website's APIs and I wanted to have a way to narrow down the search on debugging when an API failed. Therefore, each test contains two different classes that run the exact same test method but are invoked differently. (Please see the sample directory for example)

1. The monitoring class:
This class is invoked by the daemon and will write update to the database after the test finished. This class serves as a general status report of the APIs.

2. The unittest class:
This class is invoked by the `nosetests` python module that generates report and is best suit to pinpoint which testing method caused the API failure.

Because of this "two layered" way of monitoring, naming your classes and test methods is important.


How the daemon works
--------------------

+ This daemon is mainly built for the purpose of monitoring APIs and updating to database.
+ The daemon works as the following:
+ 1. It searches the given PATH for the test cases that start with **test_** and put them in a module
+ 2. For every module, find the class name that end with **monitoring**
+ 3. For every class found, test every method that start with **test_**
+ 4. Then, It checks the assertion returned from the test cases/APIs
+ 5. Update the status of that API to the database
+ 6. Do step 1~5 again after a short timeout

Instruction
-----------

On command prompt, simply type `python daemon.py PATH/TO/YOUR/TESTS` to begin monitoring the APIs
+ $ `python daemon.py sample/`
If you want to do unittest to a particular test case, run nosetests instead 
(You need to have nose installed).
+ $ `nosetests sample/test_test.py`

