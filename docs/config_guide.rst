Config Guide ***Clarification needed***
=======================================

The configuration file ''config.py'' contains variables that can be changed to implement different versions of strabo.

It contains two functions: **get_config_info()** and **config_app()**. 

get_config_info()
-----------------
The config variables are stored in a dictionary ``config_info.`` ***WHY*** This enables the information contained in the config files to be communicated between different files in a smaller format. In _______ file config_info is identified as the variable strabo_config. In HTML files (e.g. map.html) the variable straboconfig is recreated as a geojson object. 


LAYER_FIELDS and REVERSE_LAYER_FIELDS

Colors for map markers are identified in several dictionary formats. Interest point icon colors match to icon file names. Interest zone colors match to hex codes. The dropdown menu on the admin uses color names in COLOR_REP which match to icons for points and hex codes for zones. Finally, colors are stored in the database as a reversed dictionary.

config_app()
------------



.. _layer_field_config:

LAYER_FIELDS
------------

Description of how layers are stored and interact and used.
