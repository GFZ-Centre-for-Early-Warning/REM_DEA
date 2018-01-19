import sqlalchemy as db
from geoalchemy2 import Geometry

def connect(user, password, dtb, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, dtb)

    # The return value of create_engine() is our connection object
    con = db.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = db.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect('postgres', 'postgres', 'rem')

class object(db.Model):
    """
    Holds object from the asset schema.
    """
    __tablename__ = "object"
    __table_args__ = {'schema':'asset'}

    #building id
    gid = db.Column(db.Integer, primary_key=True)
    #the geometry
    the_geom = db.Column(Geometry(geometry_type='POLYGON', srid=4326))

class object_attribute(db.Model):
    """
    Holds object_attribute from the asset schema.
    """
    __tablename__ = "object_attribute"
    __table_args__ = {'schema':'asset'}

    #gid of attribute
    gid = db.Column(db.Integer, primary_key=True)
    #building id
    object_id = db.Column(db.Integer)
    #attribute code
    attribute_type_code = db.Column(db.String(254))
    #attribute value
    attribute_value = db.Column(db.String(254))
    #attribute numeric value
    attribute_numeric_1 = db.Column(db.numeric)


