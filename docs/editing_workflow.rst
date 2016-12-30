Editing Workflow
================


THIS IS ALL OUT OF DATE. USE ONLY AS A REFERENCE TO REWRITE THIS FILE.


Changing the Database
----------------------

* schema.py
    * If necessary add database column as shown in file.


* run "alembic revision -m revision_name"
* alembic/versions/revision_name.py
    * Edit so that it correctly changes the database to match the new schema
* run "alembic upgrade head"

The database should now run smoothly, assuming the revision file is of the correct format.

Now, to actually adding in is a little trickier.

Updating set_database.py:

* private_helper.py
    * edit the fill_table function
        * input: add an argument of a type that will come from and the html form via flask
        * output: a database row object with all relevant information
* set_database.py
    * add your new feature inputs into the database

In order to edit the admin interface to accomidate this change see :ref:`admin-interface-section`.


Database file structure
-----------------------

 * schema.py
    * Defines the database structure with sqlalchemy's model class
        * Takes the place of sql's CREATE TABLE statement
        * Defines relationships between tables
    * Deals with database metadata
        * Where you store list of tables
        * Stores relationships between tables and columns
 * initDB.py
    * Creates the database tables as defined in schema.py *if they do not already exist*
 * database.py
    * Helper file so that other files do not have to know the internals of sqlachemy
 * private_helper.py and public_helper.py
    * Acts as a bridge between html forms as displayed in the admin interface and the database/outgoing flask forms
        * Inputs should be flask form items
        * Outputs should be useable by flask or the database
        * Side affects should probably be somewhere else


.. _admin-interface-section:

Adding Features to the Admin Interface
--------------------------------------

Add feature to database as explained in db_edit.py

* private.py
    * Change upload_table function to have default value in argument list
    * Change show_table_upload_form to get additional information needed for feature and pass it to render_template
    * Change upload_images.html so that it displays a input form so that you can edit the feature and also give it a default value that comes from the database row so that editing will work.
    * Add feature to edit_table.html so that one can see the value there.
    * Change table_post so that it adds in html form value into private_helper's fill_table function.

Checking if all features are working
------------------------------------

* Go to /admin/upload_ips/ and add an interest point.
    * Fiddle with leaflet-draw controls and see if you can add more than one feature. If so, it is broken.
    * Continually submit the form to make sure it does not submit except when things are filled out.
        * Title
        * Icon/color
        * Layer
        * An interest point on map
        * All images fields have file uploaded.
    
