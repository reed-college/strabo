from datetime import datetime

from sqlalchemy import *
import sqlalchemy
import config
from sqlalchemy.orm import relationship

Base = sqlalchemy.ext.declarative.declarative_base()

class IdPrimaryKeyMixin:
    id = Column(Integer, primary_key=True)
    '''Unique identifier for the row'''

class DateTimeMixin:
    created_at = Column(DateTime, default=datetime.now)
    '''Time at which the row object was uploaded. Currently unused.'''

class DataType(IdPrimaryKeyMixin, DateTimeMixin):
    pass

class InterestPoints(Base,DataType):

    __tablename__ = 'interest_points'
    title = Column(Text)
    '''Title of text on the popup'''
    descrip_body = Column(Text)
    '''Body of text on the popup '''

    geojson_object = Column(Text)
    '''String that represents a `geojson object <http://geojson.org/>`_ that contains
    the location and shape of the marker, so that leaflet can easily display the interest point.'''

    layer = Column(Integer)
    '''Distinct values of thie field correspond to a distict leaflet layers, which allow the user to
    add or remove all the points of that layer  (see `Control.Layers <http://leafletjs.com/reference.html#control-layers>`_
    for more info). The layer corresponds to a name defined by the :ref:`layer_field_config`
    config value.'''

    style = Column(Text)
    '''Color identifier. Indexes COLOR_ICON, COLOR_REP, and COLOR_HEX config values'''

    images = relationship("Images",back_populates="interest_point")
    '''List of Images rows which correspond to the interest point'''

class Images(Base,DataType):
    __tablename__ = 'images'
    filename = Column(Text)
    '''Filename of the image in ``strabo/static/uploads/``. See :ref:`img_management` for more info. '''

    taken_at = Column(DateTime)
    '''Contatins month and year of the time the image was taken.'''

    ip_order_idx = Column(Integer)
    '''Contains the index of the image in the interest_point image form list.
    Used to order the images for the interst point.'''

    interest_point_id = Column(Integer, ForeignKey('interest_points.id'))
    '''Enables many to one relationship with InterestPoints.'''

    interest_point = relationship("InterestPoints",back_populates="images")
    '''Interest point row that contains image.'''

    description = Column(Text)
    '''Description that appears below image on popup.'''

    width = Column(Integer)
    '''Width of image in pixels (used by photoswipe).'''
    height = Column(Integer)
    '''Height of image in pixels (used by photoswipe).'''
