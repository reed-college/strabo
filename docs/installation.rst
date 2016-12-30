Installation Instructions
=========================

A walk-through of installing dependencies for OSX and Fedora.

Virtualenv
----------

If you havn't already, install virtualenv. `Detailed instructions on how to do so <https://github.com/reed-college/2016_sds_lesson_notes/blob/master/lesson_03_beginning_development.markdown>`_

Set up virtualenv using python 3

This can be done by::

    mkvirtualenv --python=python3 strabo

Python packages
---------------

pip install -r requirements.txt


Fedora Installation Guide
-------------------------

Packages needed::

    dnf install libjpeg-devel #allows jpeg files to be uploaded
    dnf install libpng-devel #allows png files to be uploaded
    dnf install redhat-rpm-config #needed for python modules to be installed
    dnf install python3-devel   #needed for python modules to be installed

Install virtualenv and virtualenvwrapper and set up as shown in install.md


Fedora Postgres installation
----------------------------

You will probably have to be in root user for all of this:
All taken from `<https://fedoraproject.org/wiki/PostgreSQL#User_Creation_and_Database_Creation>`_::

    dnf install postgresql-server postgresql-contrib
    systemctl enable postgresql
    postgresql-setup initdb
    systemctl start postgresql

then type in

su #log into root user, not necessary if already root user
su - postgres   # log into postgres superuser
psql #check into admin database

Then run::

    CREATE USER strabo;

    CREATE DATABASE strabo;

To allow strabo user to create and delete tables::

    ALTER USER strabo WITH SUPERUSER;

To set login with no password required find the pg_hba.conf file, with::

    cd /
    find -name "pg_hba.conf"

For me, this was at::

    ./var/lib/pgsql/data/pg_hba.conf

Open this file, scroll down to the actual table and replace ``ident`` or ``peer``
with ``trust`` on all three rows of the final collumn.

Then restart the service to take account of changes.::

    systemctl restart postgresql
