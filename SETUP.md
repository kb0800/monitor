System Requirement
-------------------

This project uses some specific modules to run monitoring tests and unittests and you need to download these modules in order to perform the tests.

*For monitoring*
+ Python: version 2.5.x or above
+ MySQLdb: [Download here](http://pypi.python.org/pypi/MySQL-python/)

*For unittest*
+ Python: version 2.5.x or above
+ nosetest: On most UNIX-like systems, you probably need to run these commands as root or using `sudo`
`$ easy_install nose`
	
	Or

`$ pip install nose`	(If you have pip installed)

Usage
------
`$ nosetests PATH/TO/YOUR/TEST`
	
