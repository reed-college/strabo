General Concepts
================

Descriptions of implementation concepts which span several files.

.. _img_management:

Image Management
----------------

When images are added to the database only one filename is stored, the name of the
saved file in the ``static/uploads`` directory. No matter what filename of the uploaded
file is, it will never overwrite a file in that directory. Instead it will
generate a random string which it appends to the filename using :py:func:`strabo.file_writing.make_unique_filename`.
Even though this file is never shown in the browser, it is still important as a reference image. If it is there, then the
resized image files can be recreated by running generate_mobile_imgs.py.

Image resizing
~~~~~~~~~~~~~~

In order to speed up our website's page load times, there are two different sizes of files which are
automatically generated from the original file. They are generated during upload and when
generate_mobile_imgs.py is run.

The smaller of the two is stored in
``static/thumbnails``, and its maximum dimensions are specified by the ``THUMBNAIL_MAX_SIZE``
configuration property. The smaller images are displayed in the popup carousel, as well as in the admin
interface.

The larger of the two is stored in
``static/mobile_imgs``. Their maximum dimensions are specified by the ``MOBILE_SERV_MAX_SIZE``
configuration property, and they are displayed the Photoswipe carousel.

Interest Point Display ***Clarification needed***
-------------------------------------------------

How interest points move from the database to being displayed by the browser.

Data permanently stored in database specified by: schema.py

When an interest point is fetched from the database to be displayed by leaflet,
in a views route (:py:func:`strabo.views.private.show_ips_upload_form` or :py:func:`strabo.views.public.map`),
it's converted to a geojson object. The geojson string is converted into an
object, and the entries in the row are all moved into the properties attribute of
the newly created object. See :py:func:`strabo.geojson_wrapper.make_other_attributes_properties`
for more details.

A list of these objects representing all the interest points for display
is assigned to a javascript variable in a jinja template (map.html and upload_ips.html).

Now, this list of geojson objects is converted into a Leaflet FeatureGroup,
which many functions interact with to display the interest points.

Authentication and Authorization
--------------------------------

Authentication and authorization for strabo was set up with the help of Reed's Computiner & Information Services (CIS). Access to the private end of strabo (the /admin web pages) require a Kerberos login and password. Only specific users can access the admin pages. Adding users to the list involves contacting CIS or adding username/password pairs to the remote server using an ssh key. 

