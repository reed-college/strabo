import enum
import os

# set feature types for uploading interest points
class Layers(enum.Enum):
    plant = 1
    animal = 2
    hist = 3
    cool = 4

def get_config_info():
    config_info = dict()

    #
    #
    #
    ###### The following variables require configuration.
    # set the latitude and longitude for the center of the map
    # these values will be passed into the js file that gets rewritten
    # each time interest points are updated by the administrator, so
    # changes here will not be reflected until an interest point is
    # added, edited, or deleted.
    config_info['LAT_SETTING'] = 45.481851
    config_info['LONG_SETTING'] = -122.630397
    config_info['INITIAL_ZOOM'] = 17

    config_info['LAYER_FIELDS'] = [
        "Plants",
        "Animals",
        "Interest Points",
        "Sensitive Areas"
    ]

    # Finds the location of the /strabo/static file
    config_info['MAP_ICONS'] = [fname for fname in os.listdir(os.path.realpath("./strabo/static/map_icons/"))]

    #config_info['MAP_ICONS'] = [fname for fname in os.listdir("/Users/avakamb/strabo/strabo/strabo/static/map_icons/")]

    #
    ##### set preferred styles, website title, and headings
    ##### "About" page ("about.html") must be edited directly.

    config_info['BASE_CSS'] = "canyon_base.css"
    config_info['HEADER_CSS'] = "header.css"
    config_info['FOOTER_CSS'] = "footer.css"
    config_info['MAP_CSS'] = "map.css"
    config_info['GALLERY_CSS'] = "gallery.css"
    config_info['ABOUT_CSS'] = 'about.css'

    config_info['WEBSITE_TITLE'] = 'Discover the Reed College Canyon'
    config_info['INDEX_GREETING'] = "Select a tab to begin adding content to the Canyon."

    # set title and subtitle for image gallery
    config_info['GALLERY_TITLE'] = "Image Gallery"
    config_info['GALLERY_SUBTITLE'] = "Reed College Canyon Past and Present"

    config_info['MAP_TEMPLATE'] = "map.html"
    config_info['BASE_TEMPLATE'] = "base.html"
    config_info['HEADER_TEMPLATE'] = "header.html"
    config_info['FOOTER_TEMPLATE'] = "footer.html"

    config_info['MAP_JS'] = 'map.js'
    config_info['ADMINMAP_JS'] = 'drawMap.js'
    config_info['FAVICON'] = '../strabo/strabo/static/favicon.ico'


    ###### The following variables probably will not require configuration.
    # set absolute and relative paths to the upload directory for images
    config_info['UPLOAD_FOLDER'] = '../strabo/strabo/static/uploads/'
    config_info['UPLOAD_FOLDER_RELPATH'] = '/static/uploads/'
    # set absolute and relative paths to the upload directory for thumbnails
    config_info['NEW_DATA_DIRECTORY'] = '../strabo/strabo/static/thumbnails/'
    config_info['NEW_DATA_DIRECTORY_RELPATH'] = '/static/thumbnails/'
    # set folder name for javascript
    config_info['JS_FOLDER'] = '../strabo/strabo/static/js/'


    # set absolute and relative paths to styles
    config_info['PATH_TO_PUBLIC_STYLES'] = "../static/public_styles/"
    config_info['RELPATH_TO_PUBLIC_TEMPLATES'] = "public/"

    config_info['ALLOWED_EXTENSIONS'] = ['png','PNG','jpg', 'jpeg', 'JPG', 'JPEG']

    config_info["MAP_TILE_SRC"] = 'http://{s}.tile.thunderforest.com/outdoors/{z}/{x}/{y}.png'
    config_info['LEAFLET_ATTRIBUTES'] = {
        "attribution":'Map tiles by Thunderforest, Map data by OpenStreetMap',
        "minZoom": 14,
        "maxZoom": 22,
        "ext": 'png'
    }

    config_info["THUMBNAIL_MAX_SIZE"] = (300,250)#max_width, max_height

    return config_info


def config_app(app):
    '''
    Flask and sqlachemy specific configurations. These are kept seperate
    becuase unlike the others, they will change between development and deployment.
    '''
    app.config['SQLALCHEMY_DATABASE_URI']  = "postgres://localhost/strabo"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
    app.config['DEBUG']  = True