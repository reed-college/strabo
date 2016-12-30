Install Help Guide
==================

At the bottom is a
help guide for specific errors. This file is here to deal with
all the problems of installing and setting up strabo. Please feel free to add any
solutions to any installation issues you had on your system getting strabo up and running.

OSError: cannot decode filename
-------------------------------

If you ever get an error that looks like the above, this means
you do not have the system library that decodes images set up on
your computer. You will have to uninstall the python package Pillow, install the
system library and reinstall Pillow. For jpeg files on OSX, this
can be done with brew by::

    pip uninstall Pillow
    brew install libjpeg #ubuntu: apt-get install libjpeg-dev
    pip install  --no-cache-dir -I Pillow

This error occurs when you installed Pillow before the system library as well, or randomly on OSX.
If the system library is already installed you just need to do steps 1 and 3.

On other systems, the process should be very similar, but the
specific package and package system will be different.

Other image formats (png?) might also have a similar problem.

Geojson module has no attribute error
-------------------------------------

This error may be outdated.

This most likely means you are using python2. Use python 3 as
shown above. The easiest way to do this is by removing the old
virtualenv and making a new one using python 3::

    deactivate
    rmvirtualenv strabo

Then set up new virtualenv as show in the ordinary installation guide.
