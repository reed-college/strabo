Javascript
==========

Documentation for the Javascript files found in /strabo/static/js/.

map_info.js
-----------

Helper code required by ``map.js`` and ``drawmap.js``.

Extensively uses the `Leaflet library <http://leafletjs.com/>`_ and so the documentation
for this file contains links to their documentation whenever appropriate.

.. js:class:: ColorIcon(icon_options)

    :param object icon_options: Options are described `here <http://leafletjs.com/reference.html#icon>`_.

    Extends `L.Icon <http://leafletjs.com/reference.html#icon>`_.

    Allows one to create icons of a defined size by passing in
    iconUrl as an option.
    ***clarification needed*** is ColorIcon really a class? I don't see that in the API

    Example:

    .. code-block:: javascript

        var myicon = new ColorIcon({iconUrl:'/static/map_icons/Green.png'});

.. js:data:: locateIcon

    Leaflet icon object that marks user location.

.. js:data:: icon_objs

    Dictionary mapping icon image filenames to the ColorIcon object that
    uses that file as its marker. The filenames are stored in the config file COLOR_ICON.

.. js:function:: make_map(map_container_id)

    :param string map_container_id: id of the HTML div that will contain the map.

    Creates leaflet map with latitude, longitude, and initial zoom
    settings described in config.

.. js:function:: add_tile_to(map)

    :param map: Leaflet map.

    Adds tile source according to MAP_TILE_SRC config value, allowing the map
    tiles to be loaded.

    Adds leaflet attributes footer with the text specified by LEAFLET_ATTRIBUTES.

.. js:function:: make_all_layers_group(interest_point_geojson_list)
    ***clarification needed*** isn't calling this parameter "interest_point_geojson_list" an example of bad hungarian notation??

    :param interest_point_geojson_list: List of geojson objects that are passed in.
    :returns: An `L.FeatureGroup <http://leafletjs.com/reference.html#featuregroup>`_,
        which is the form other helper functions expect the interest_point data to be in.

.. js:function:: set_styles(all_layers_group)

    :param L.FeatureGroup all_layers_group:
        Contains interest point data.

    This function separates interest points that are of the "Point" GeoJSON type from interest points that are of the "Polygon" GeoJSON type (aka zones).

    Zones are styled with standard weight, dashArray and fillOpacity. The color is identified by the config dictionary COLOR_HEX which maps to a specific hexadecimal code for that color. 

    Points are styled with a marker icon from the icon_objs dictionary. The dictionary maps colors to the filename for the colored marker icon.

.. js:function:: place_overlays_on(all_layers_group,map)

    :param map: Leaflet map.
    :param L.FeatureGroup all_layers_group:
        Contains interest point data.

    RESTRICTION: Cannot have already been added to the map. ***clarification needed*** do you mean, it cannot be called more than once?

    Creates a leaflet `Control.Layers <http://leafletjs.com/reference.html#control-layers>`_
    which allows one to selectively remove and add groups of interest points ("layers") from the map.

    Layer by layer adds all_layers_group to the map.

    The names of the layers correspond to the names in the config value LAYER_FIELDS.
    See :ref:`layer_field_config` documentation for more information.

.. js:function:: bind_popups(all_layers_group)

    :param L.FeatureGroup all_layers_group:
        Contains interest point data.

    Makes all interest points in all_layers_group open up a default leaflet popup upon being clicked. The default popup will display the interest point name.

map.js
------

Loaded by the main map page.

.. js:function:: set_feature_click(all_layers_group)

    :param L.FeatureGroup all_layers_group:
        L.FeatureGroup `information <http://leafletjs.com/reference.html#featuregroup>`_.
        Contains interest point data.
    
    Sets all interest points in all_layers_group to call :js:func:`ip_clicked(db_id)` when clicked,
    passing in the interest point's id as the argument.

drawMap.js
----------

The admin map that is loaded by the upload_ips page.

This file displays a map which the administrator can use to pick an interest point
location by hand.

It shares map configuration properties with map.js via map_info.js functions.

.. js:function:: set_draw_controls(drawMap,drawnItems)

    :param string message_identifier: A jquery selector string (like "#map-form-issue") which points to the error message that is shown
        when the input field is invalid.


popup.js
--------

Loaded by the main map page.


Flickity
~~~~~~~~

This uses the `Flickity library <http://flickity.metafizzy.co/>`_
to render the photo gallery that is displayed in the
main popup.

Photoswipe
~~~~~~~~~~

When flickity carousel items are clicked, it opens a
`Photoswipe photo gallery <http://photoswipe.com/>`_ that allows you to
view larger pictures.


upload_ips.js
-------------

Form Validation
~~~~~~~~~~~~~~~

Strabo does not use any external form validation framework. It does everything itself
for maximum flexibility and simplicity.

Input fields are checked with the builtin form object that is passed into checkForm.
You can access the html field by the attribute of the object that corresponds to
the ``name`` html attribute.

Here is an example which checks if the value of an input is the default value (recall that the
the string typed into the input box is the value of the input element).

.. code-block:: html

    <input name="icon" value="default-icon"></input>

.. code-block:: javascript

    var is_default_value = form.icon.value == "default-icon"

As you can see, for input fields this is very strait forward. For other types of data entry, like
select and checkbox, are more difficult. ***clarification needed*** (Generally it is bad form to write that things are "straightforward" "just" or "difficult/easy." See if you can find another way to phrase the previous line/) `This page <http://www.the-art-of-web.com/javascript/validate/>`_
explains how to work with many of these types in detail.

In order to show the user what is wrong with the form, you can place error messages in the
html and mark them as hidden, so that they don't appear when the page first loads.

Here is an example from upload_ips.html

.. code-block:: html

    <p id="map-form-issue" class="form-error" hidden>Must place a new object on the map.</p>

Then you can add an InputField which knows about that message.

.. js:class:: InputField(message_identifier, is_valid_cond)

    Corresponds with a user input field.

    :param string message_identifier: A jquery selector string (like "#map-form-issue") which points to the error message that is shown
        when the input field is invalid.
    :param function(form) is_valid_cond: a function with takes a form object and returns whether the corresponding input field
        is valid.


***clarification needed*** how does this tie into the class above? a sentence that connects the InputFields and the validators would be nice.
.. js:data:: validators

    List of InputField objects which together describe all the contents of the form.

.. js:function:: checkForm(form)

    Called with inline javascript in ``upload_ips.html``.

    Iterates through input fields. If they are invalid, shows the corresponding
    html error message which explains what is wrong with the form. If they are valid, hides the form. ***clarification needed*** what do you mean it "hides the form"

    :param form: Special builtin form object.
    :returns: Whether the form is valid or not. If false, then the form is not submitted.


Upload Preview
~~~~~~~~~~~~~~

.. js:function:: enable_file_upload_preview($div)

    When the file input field is changed when the user uploads an image, it
    uses :js:func:`showUploadImg` to display that image. ***clarification needed*** why is this function called "enable_file_upload_preview"? why not something like file upload change or whatever

.. js:function:: showUploadImg($div,input)

    :param JQuery $div: Image upload form div.
    :param DOM-object input: Image input div.

    Reads the image from ``input`` and displays it in the $div's preview element.


Dynamic Image Uploading
~~~~~~~~~~~~~~~~~~~~~~~

``templates/private/upload_img_model.html`` contains a hidden div which serves as a
model for the image upload interface. When divs are added (or "Add Image Below" is clicked), it clones the div,
removes the model class (so that it is differentiable from the actual model), removes the hidden attribute, changes the date placeholder to the current day, and adds event handlers for the buttons.

As the image form divs are added, they form a linked list. In html, the list takes the form of a sequence of divs.

Each add and delete button has its own event handler, which has knowledge of its parent
div. Pressing the Delete button deletes the current img div and pressing the Add Below
button will insert another image form in between it and the next div.


.. js:function:: $new_img_div()

    Clones a new div from the img-model and turns it into a JQuery ***clarification needed*** (a jQuery what?) that will correctly
    display the image form. Does not add it to the DOM.

    Notably, it sets the date placeholder so that it displays the default upload date (today).
    The mechanics of adding the default to the database happens in :py:func:`strabo.private_helper.make_date`.


.. js:function:: initalize_edit_images()

    Purpose: Allows editing of interest point images.

    Global Input: ``ip_images``, a javascript object passed in from a jinja
    template in upload_ips.html. It is a list of objects with attributes corresponding to
    the columns in the :py:class:`strabo.schema.Images` plus ``month`` and ``year`` attributes pulled from
    the taken_at column.

    Requirement: Any parts of the form should be submitted identically to how they were first uploaded. ***clarification needed*** what does this mean

    Creates and displays a list of image form divs representing the images
    described by ip_images.



