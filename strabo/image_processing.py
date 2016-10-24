'''
Handles interaction with `PIL library <https://python-pillow.org/>`_, including thumbnail creation, dimension getting, and
image processing capabilities, including allowed file extensions.
'''

import os
from PIL import Image

from strabo import utils

from strabo import app
from strabo import straboconfig

def allowed_file(filename):
    '''Checks whether the filename has an extension that is listed in ALLOWED_EXTENSIONS config value.'''
    return utils.get_extension(filename) in straboconfig['ALLOWED_EXTENSIONS']

def save_shrunken_image(image_path,thumbnail_path,max_dim):
    '''
    Uses the Python Imaging Library to save a smaller image of the same scale but
    with maximum dimensions specified by max_dim using the
    `thumbnail method <http://pillow.readthedocs.io/en/3.3.x/reference/Image.html?highlight=thumbnail>`_.

    :param string image_path: File path (including filename) of source image (must be a valid image file)
    :param string thumbnail_path: File path (including filename) of location image will be saved
    :param max_dim: (width,height) Tuple specifiying maximum dimensions for output image
    '''
    # import desired image from /uploads folder
    with Image.open(image_path) as img:
        # create a thumbnail from desired image
        # the thumbnail will have dimensions of the same ratio as before, capped by
        # the limiting dimension of max_dim
        img.thumbnail(max_dim,Image.ANTIALIAS)
        # save the image under a new filename in thumbnails directory
        img.save(thumbnail_path)

def get_dimensions(filename):
    '''Get dimensions of image with ``filename`` in ``static/uploads/`` folder.'''
    with Image.open(os.path.join(straboconfig['UPLOAD_DIR'],filename)) as im:
        return im.size #width, height tuple
