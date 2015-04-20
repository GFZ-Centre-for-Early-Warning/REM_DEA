from flask.ext.wtf import Form
from wtforms.fields import TextField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
import wtforms.validators as validators
from models import ve_resolution1, dic_attribute_value
   
def getMatType():
	return dic_attribute_value.query.filter_by(attribute_type_code='MAT_TYPE')
def getMatProp():
	return dic_attribute_value.query.filter_by(attribute_type_code='MAT_PROP')


class RrvsForm(Form):
	"""
	This Form class contains all of the fields in the RRVS form.
	"""
	# Text fields
	gid_field = TextField(label="BuildingID")
	height_field = TextField(label="Height", validators=[validators.Length(max=10), validators.Required()])
	# Select fields
	mat_type_field = QuerySelectField("Material Type", query_factory=getMatType, get_label='description', allow_blank=True)
	mat_prop_field = QuerySelectField("Material Property", query_factory=getMatProp, get_label='description', allow_blank=True)
	# Submit field
	submit = SubmitField("Send")
