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


Quick start
-----------

You can build an image tagged *deps* from this Dockerfile by running:

`docker build -t deps .`

Then, run a container named *deps* based in the built image by executing:

`docker run --name deps -t -d deps`

To check the container is properly running, execute this:

`docker ps`

You will see an output like this:

.. code-block:: bash

    CONTAINER ID   IMAGE     COMMAND     CREATED         STATUS         PORTS     NAMES
    e5014d217bd7   deps      "python3"   3 seconds ago   Up 2 seconds             deps


To open a bash shell in the container:

`docker exec -it deps /bin/bash`


How to execute
--------------

To execute the dependencies manager using the sample input file included in this repo just run:

`docker run --rm deps python /usr/dependency_manager/app/deps_manager.py /usr/dependency_manager/data/sample_input.txt`

You will see an output like this

.. code-block:: python

    DEPEND TELNET TCPIP NETCARD
    DEPEND TCPIP NETCARD
    DEPEND DNS TCPIP NETCARD
    DEPEND BROWSER TCPIP HTML
    INSTALL NETCARD
        NETCARD successfully installed
    INSTALL TELNET
        TCPIP successfully installed
        TELNET successfully installed
    INSTALL foo
        foo successfully installed
    REMOVE NETCARD
        NETCARD is still needed
    INSTALL BROWSER
        HTML successfully installed
        BROWSER successfully installed
    INSTALL DNS
        DNS successfully installed
    LIST
        HTML
        BROWSER
        DNS
        NETCARD
        foo
        TCPIP
        TELNET
    REMOVE TELNET
        TELNET successfully removed
    REMOVE NETCARD
        NETCARD is still needed
    REMOVE DNS
        DNS successfully removed
    REMOVE NETCARD
        NETCARD is still needed
    INSTALL NETCARD
        NETCARD is already installed
    REMOVE TCPIP
        TCPIP is still needed
    REMOVE BROWSER
        BROWSER successfully removed
        HTML is no longer needed
        HTML successfully removed
        TCPIP is no longer needed
        TCPIP successfully removed
    REMOVE TCPIP
        TCPIP is not installed
    LIST
        NETCARD
        foo
    END


How to run tests
-----------------

To run the included tests execute:

`docker run --rm deps pytest /usr/dependency_manager/tests`

How to run linter

To run flake8 linter, execute:

`docker run --rm deps flake8 /usr/dependency_manager/app`

Credits
-------

Created by Jorge Arévalo <jorgeas80@gmail.com>
