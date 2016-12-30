Javascript
==========


map_info.js
-----------

Helper code required by ``map.js`` and ``drawmap.js``.

Extensively uses the `Leaflet library <http://leafletjs.com/>`_ and so the documentation
for this file contains links to their documentation whenever appropriate.

.. js:class:: ColorIcon(icon_options)

    :param object icon_options: Options are described `here <http://leafletjs.com/reference.html#icon>`_

    Extends `L.Icon <http://leafletjs.com/reference.html#icon>`_

    Allows one to create icons of the hard-coded size by simply passing in
    iconUrl as an option.

    Example:

    .. code-block:: javascript

        var myicon = new ColorIcon({iconUrl:'/static/map_icons/Green.png'});

.. js:data:: locateIcon

    Leaflet icon object that marks user location.

.. js:data:: icon_objs

    Dictionary mapping all icon filenames to the ColorIcon object that
    uses that file as its marker.

.. js:function:: make_map(map_container_id)

    :param string map_container_id: Id of the HTML div that will contain the map.

    Creates leaflet map with latitude, longitude, and initial zoom
    settings described in config.

.. js:function:: add_tile_to(map)

    :param map: Leaflet map.

    Adds tile source according to MAP_TILE_SRC config value, allowing the map
    tiles to be loaded.

    Adds leaflet attributes footer with the text specified by LEAFLET_ATTRIBUTES
    to the bottom of the map.

.. js:function:: make_all_layers_group(interest_point_geojson_list)

    :param interest_point_geojson_list: List of geojson objects that are passed in.
    :returns: A `L.FeatureGroup <http://leafletjs.com/reference.html#featuregroup>`_
        which is the form other helper functions expect the interest_point data to be in.

.. js:function:: set_styles(all_layers_group)

    :param `L.FeatureGroup <http://leafletjs.com/reference.html#featuregroup>`_ all_layers_group:
        Contains interest point data.

    For all interest points which are of the "Polygon" geojson type, it sets the
    style to a hard-coded value.

    For interest points which are of the "Point" geojson type (regular
    interest points) it sets the marker icon specified by the icon filename
    associated with the interest point.

.. js:function:: place_overlays_on(all_layers_group,map)

    :param map: Leaflet map.
    :param `L.FeatureGroup <http://leafletjs.com/reference.html#featuregroup>`_ all_layers_group:
        Contains interest point data.

        RESTRICTION: Cannot have already been added to the map.

    Creates a leaflet `Control.Layers <http://leafletjs.com/reference.html#control-layers>`_
    which allows one to selectively remove and add groups of interest points called
    "layers" from the map.

    Adds all_layers_group to the map in pieces corresponding to the layers.

    The names of the layers correspond to the names in the config value LAYER_FIELDS.
    See :ref:`layer_field_config` documentation for more information.

.. js:function:: bind_popups(all_layers_group)

    :param `L.FeatureGroup <http://leafletjs.com/reference.html#featuregroup>`_ all_layers_group:
        Contains interest point data.

    Makes all interest points in all_layers_group bring up a default leaflet popup
    when clicked displaying the interest point name.


map.js
------

Loaded by the main map page.

.. js:function:: set_map_click(map)

    Makes it so that whenever the map is clicked,
    a popup is opened displaying the latitude and longitude of the location
    that was clicked.

.. js:function:: set_feature_click(all_layers_group)

    :param `L.FeatureGroup <http://leafletjs.com/reference.html#featuregroup>`_ all_layers_group:
        Contains interest point data.

    Sets all interest points in all_layers_group to call :js:func:`ip_clicked(db_id)` when clicked
    passing in the interest point's id as the argument.

drawMap.js
----------

Loaded by the upload_ips page.

This file displays a map which the administrator can use to pick an interest point
location by hand.

It shares map configuration properties with map.js via map_info.js functions

.. js:function:: set_draw_controls(drawMap,drawnItems)

    :param string message_identifier: A jquery selector string (like "#map-form-issue") which points to the error message that is shown
        when the input field is valid.


popup.js
--------

Loaded by the main map page.


Flickty
~~~~~~~

This uses the `flickety library <http://flickity.metafizzy.co/>`_
to render the photo gallery that is displayed in the
main popup.

Photoswipe
~~~~~~~~~~

When flickty carousel items are clicked, it opens a
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

Here is an example which checks if the value of an input is the default value (Recall that the
the string typed into the input box is the value of the input element).

.. code-block:: html

    <input name="icon" value="default-icon"></input>

.. code-block:: javascript

    var is_default_value = form.icon.value == "default-icon"

As you can see, for input fields this is very strait forward. For other types of data entry, like
select and checkbox, are more difficult. `This page <http://www.the-art-of-web.com/javascript/validate/>`_
explains how to work with many of these types in detail.

In order to show the user what is wrong with the form, you can place error messages in the
html where you would want them to display, and mark them as hidden, so that they don't display
when the page first loads.

Here is an example from upload_ips.html

.. code-block:: html

    <p id="map-form-issue" class="form-error" hidden>Must place a new object on the map.</p>

Then you can just add an InputField which knows about that message.

.. js:class:: InputField(message_identifier, is_valid_cond)

    Corresponds with a user input field.

    :param string message_identifier: A jquery selector string (like "#map-form-issue") which points to the error message that is shown
        when the input field is valid.
    :param function(form) is_valid_cond: a function with takes a form object and returns whether the corresponding input field
        is valid.

.. js:data:: validators

    List of InputField objects which together describe all the contents of the form.

.. js:function:: checkForm(form)

    Is called with inline javascript in upload_ips.html.

    Iterates through input fields, and if they are invalid, shows the corresponding
    html error message which explain what all is wrong with the form, or if they are valid, hides the form.

    :param form: Special builtin form object.
    :returns: Whether the form is valid or not. If it returns false, then the form is not submitted.

Upload Preview
~~~~~~~~~~~~~~

.. js:function:: enable_file_upload_preview($div)

    When the file input field is changed, by the user uploading and image, it
    uses :js:func:`showUploadImg` to display that image.

.. js:function:: showUploadImg($div,input)

    :param JQuery $div: Image upload form div.
    :param DOM-object input: Image input div.

    Reads the image from ``input`` and displays it on the on the $div's preview element.
    

Dynamic Image Uploading
~~~~~~~~~~~~~~~~~~~~~~~

Also handles almost everything to do with the the dynamic image loading form.

``templates/private/upload_img_model.html'' contains a hidden div which serves as a
prototype for the image upload interface. When divs are added, it clones the div,
removes the prototype class (so that it is differentiable from the actual prototype)
and hidden attribute (so that it shows up on the screen), changes the date placeholder to the current day
and adds event handlers for the buttons.

As the image form divs are added, they form a linked list, which, since it is html,
takes the form of a sequence of divs::

Each add and delete button has its own event handler, which has knowledge of its parent
div. Pressing the Delete button deletes the current img div and pressing the Add Below
button will insert another image form in between it and the next div.


.. js:function:: $new_img_div()

    Clones a new div from the img-model and turns it into a JQuery that will correctly
    display the image form. Does not add it to the DOM.

    Notably, it sets the date placeholder so that it displays the default upload date (today).
    The mechanics of adding the default to the database happens in :py:func:`strabo.private_helper.make_date`.

.. js:function:: initalize_edit_images()

    Purpose: Allows editing of interest point images.

    Global Input: ``ip_images``, a javascript object passed in by server from a jinja
    template in upload_ips.html. Is a list of objects with attributes corresponding to
    the columns in the :py:class:`strabo.schema.Images` plus ``month`` and ``year`` attributes pulled from
    the taken_at column.

    Requirement: Any parts of the form should be submitted identically to how they were first uploaded.

    Creates and displays a list of image form divs representing the images
    described by ip_images.






..
