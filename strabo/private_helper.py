'''
Assigns entries in the table accoring to text input from the admin interface.
'''
import werkzeug
import os
import datetime

from strabo import schema
from strabo import image_processing
from strabo import utils
from strabo import file_writing

from strabo import app
from strabo import db
from strabo import straboconfig

def fill_interest_point(ip,image_ids,form_title,form_body,form_geo_obj,form_layer,form_icon):
    if not ip.id:
        raise RuntimeError("ip needs to be stored in database to be filled")
    ip.title = form_title
    ip.descrip_body = form_body
    ip.geojson_object = form_geo_obj
    ip.layer = straboconfig["REVERSE_LAYER_FIELDS"][form_layer]
    ip.icon = form_icon + ".png" # adds back icon extension (png) from admin input form
    ip.images = [db.session.query(schema.Images).get(int(id)) for id in image_ids]

def fill_image(image,form_file,form_descrip,year,month):
    '''
    If a flask.files object (see `here <http://flask.pocoo.org/docs/0.11/patterns/fileuploads/>`_ for more information)
    is passed in, then it saves the new file and stores the new information in the database.
    If the image row already stored information about an old image (the image was edited), then that old image is deleted.
    '''
    image.taken_at = datetime.date(utils.safe_pos_int_conv(year),utils.safe_pos_int_conv(month),1)
    image.description = form_descrip

    if form_file:
        if image.filename:
            file_writing.delete_image_files(image.filename)

        image.filename = file_writing.make_filename(form_file.filename)
        file_writing.save_image_files(form_file,image.filename)
        image.width,image.height = image_processing.get_dimensions(image.filename)
