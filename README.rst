====================
Dependencies manager
====================

Implementation of a program to automate the process of adding and removing software packages

* Free software: MIT license
* Documentation:


Features
--------

* Maintain a record of installed packages and their dependencies.
* Support explicitly installing a package in response to a command (unless it is already installed).
* Support implicitly installing a package if it is needed to install another package.
* Support explicitly removing a package in response to a command (if it is not needed to support other packages).
* Support implicitly removing a package if it is no longer needed to support another component and was not explicitly installed.


How to execute
--------------

You can build an image tagged _deps_ from this Dockerfile by running

`docker build -t deps`


Credits
-------

Created by Jorge Arévalo <jorgeas80@gmail.com>
