#############
RevSquare GIT
#############

Manages git interactions on projects. Offers a few set of management commands to quickly synchronize code. This is mostly for usage of RevSquare's developpment teams.

*******
Install
*******

From Github

.. code-block::  shell-session

    https://github.com/RevSquare/rs_git#egg=rs_git


*****
Setup
*****


The first step is to add the app in your installed apps list in settings.py

.. code-block::  python

    INSTALLED_APPS = (
        ...
        'rs_git'
        ...
    )

Then you can declare some settings of your GIT environment in your settings.py file

Location of your local pip requirements files, for exemple:

.. code-block::  python

    RSGIT_REQUIREMENTS_FILE = 'requirements/local.txt'

Your main project developpment branch, for exemple:

.. code-block::  python

    RSGIT_DEVELOPPMENT_BRANCH = 'develop'

In case you have a frontend subtree, you can use the RSGIT_FRONTEND dictionnary, for exemple:

.. code-block::  python

    RSGIT_FRONTEND = {
        'branch': 'master',
        'remote': 'static',
        'path': 'myproject/frontend'
    }



*************
Command usage
*************

If all you settings variables listed above are informed, you can simply go with:

.. code-block::  shell

    python manage.py git_sync

Otherwise you can use specific options, here are the available options with exemples:

.. code-block::  shell

    python manage.py git_sync --branch 'develop'  --remote 'origin' --requirements 'myproject/frontend'



************
Contribution
************


Please feel free to contribute. Any help and advices are much appreciated.


*****
LINKS
*****

Development:
    https://github.com/RevSquare/rs_git
