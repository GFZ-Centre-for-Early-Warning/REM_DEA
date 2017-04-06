'''
---------------------------
    models.py
---------------------------
Created on 24.04.2015
Last modified on 13.01.2016
Author: Marc Wieland, Michael Haas
Description: Defines the database model
----
'''
from webapp import db
from flask.ext.security import RoleMixin, UserMixin
from geoalchemy2 import Geometry
from sqlalchemy.dialects import postgresql

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('users.users.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('users.roles.id')),
        schema = 'users')

class Role(db.Model, RoleMixin):
    """
    Role for database
    """
    __tablename__="roles"
    __table_args__ = {'schema':'users'}

    id = db.Column(db.Integer(), primary_key=True)
    name = ''

class User(db.Model, UserMixin):
    """
    User for RRVS
    """
    __tablename__="users"
    __table_args__ = {'schema':'users'}

    id = db.Column(db.Integer(), primary_key=True)
    authenticated = db.Column(db.Boolean, default=False)
    password = ''

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the taskid to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class task(db.Model):
    """
    Holds the tasks from the users schema.
    """
    __tablename__="tasks"
    __table_args__ = {'schema':'users'}

    id = db.Column(db.Integer, primary_key=True)
    bdg_gids = db.Column(postgresql.ARRAY(db.Integer))
    img_ids = db.Column(postgresql.ARRAY(db.Integer))

class tasks_users(db.Model):
    """
    Holds the assigned tasks for all users
    """
    __tablename__="tasks_users"
    __table_args__ = {'schema':'users'}

    user_id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer)


class dic_attribute_value(db.Model):
    """
	Holds dic_attribute_value from the taxonomy schema.
	"""
    __tablename__ = "dic_attribute_value"
    __table_args__ = {'schema':'taxonomy'}

    gid = db.Column(db.Integer, primary_key=True)
    attribute_type_code = db.Column(db.String(254))
    attribute_value = db.Column(db.String(254), unique=True)
    description = db.Column(db.String(254))
    description_ar = db.Column(db.String(254))
    extended_description = db.Column(db.String(1024))

class ve_object(db.Model):
    """
    Holds ve_object from the asset schema.
    """
    __tablename__ = "ve_object"
    __table_args__ = {'schema':'asset'}

    gid = db.Column(db.Integer, primary_key=True)
    mat_type = db.Column(db.String(254))
    mat_tech = db.Column(db.String(254))
    mat_prop = db.Column(db.String(254))
    llrs = db.Column(db.String(254))
    llrs_duct = db.Column(db.String(254))
    height = db.Column(db.String(254))
    height2 = db.Column(db.String(254))
    height_1 = db.Column(db.Integer)
    height2_1 = db.Column(db.Integer)
    yr_built = db.Column(db.String(254))
    year_1 = db.Column(db.Integer)
    year_2 = db.Column(db.Integer)
    occupy = db.Column(db.String(254))
    occupy_dt = db.Column(db.String(254))
    position = db.Column(db.String(254))
    plan_shape = db.Column(db.String(254))
    str_irreg = db.Column(db.String(254))
    str_irreg_2 = db.Column(db.String(254))
    str_irreg_dt = db.Column(db.String(254))
    str_irreg_dt_2 = db.Column(db.String(254))
    str_irreg_type = db.Column(db.String(254))
    str_irreg_type_2 = db.Column(db.String(254))
    nonstrcexw = db.Column(db.String(254))
    roof_shape = db.Column(db.String(254))
    roofcovmat = db.Column(db.String(254))
    roofsysmat = db.Column(db.String(254))
    roofsystyp = db.Column(db.String(254))
    roof_conn = db.Column(db.String(254))
    floor_mat = db.Column(db.String(254))
    floor_type = db.Column(db.String(254))
    floor_conn = db.Column(db.String(254))
    foundn_sys = db.Column(db.String(254))
    rrvs_status = db.Column(db.String(254))
    vuln = db.Column(db.String(254))
    comment = db.Column(db.String(254))
    the_geom = db.Column(Geometry(geometry_type='POLYGON', srid=4326))

class pan_imgs(db.Model):
    """
    Holds panoramic images from the database
    NOTE: right now only name of file on hdd
    """
    __tablename__ = "img"
    __table_args__ = {'schema':'image'}

    gid = db.Column(db.Integer, primary_key=True)
    gps = db.Column(db.Integer)
    repository = db.Column(db.String(255))
    filename = db.Column(db.String(100))
    frame_id = db.Column(db.Integer)
    source = db.Column(db.String(254))

class gps(db.Model):
    """
    Holds locations of the panoramic images from the database
    """
    __tablename__ = "gps"
    __table_args__ = {'schema':'image'}

    gid = db.Column(db.Integer, primary_key=True)
    #img_id = db.Column(db.Integer)
    azimuth = db.Column(db.Float)
    the_geom = db.Column(Geometry(geometry_type='POINT',srid=4326))

class t_object(db.Model):
    """
    Holds object from the asset schema.
    """
    __tablename__ = "object"
    __table_args__ = {'schema':'asset'}

    #building id
    gid = db.Column(db.Integer, primary_key=True)
    #survey_gid
    survey_gid = db.Column(db.Integer)
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
    attribute_numeric_1 = db.Column(db.Numeric)

class survey(db.Model):
    """
    Holds object_attribute from the asset schema.
    """
    __tablename__ = "survey"
    __table_args__ = {'schema':'survey'}

    #gid of attribute
    gid = db.Column(db.Integer, primary_key=True)
    #name of survey
    name = db.Column(db.String(254))

class Boundary_types(db.Model):
    """
    Holds boundary_types from the boundaries schema.
    """
    __tablename__ = "boundary_types"
    __table_args__ = {'schema':'boundaries'}

    #gid of attribute
    gid = db.Column(db.Integer, primary_key=True)
    #type of boundary
    type = db.Column(db.String(20))

class Boundaries(db.Model):
    """
    Holds boundaries from the boundaries schema.
    """
    __tablename__ = "boundaries"
    __table_args__ = {'schema':'boundaries'}

    #gid of attribute
    gid = db.Column(db.Integer, primary_key=True)
    #type of boundary
    types = db.Column(db.String(20))
    #the geometry
    geom = db.Column(Geometry(geometry_type='POLYGON', srid=4326))



