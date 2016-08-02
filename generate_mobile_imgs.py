'''
Overwrites thumbnails and mobile_imgs files with files of size specified in
configuration values THUMBNAIL_MAX_SIZE and MOBILE_SERV_MAX_SIZE, respectively.

Use whenever the dimentions specified by either of those values have been changed.
'''

import os

from strabo import utils
import config
from strabo import file_writing
from strabo import image_processing

from strabo import straboconfig

utils.fill_dict_with(straboconfig,config.get_config_info())

for filename in os.listdir(os.path.realpath("./strabo/static/uploads/")):
    if image_processing.allowed_file(filename):
        file_writing.save_shrunken_images_with(filename)
