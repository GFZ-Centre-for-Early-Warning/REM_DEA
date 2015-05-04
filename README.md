Remote Rapid Visual Screening (RRVS) Tool
=========================================


INSTALLATION
------------

In order to run the application locally do the following:

A) Setup virtualenvironment and add the project source code
1. $ sudo pip install virtualenv
2. go to root of project folder and run $ virtualenv flaskapp
   this creates a new folder to hold the virtualenvironment
3. cd to flaskapp and run $ . bin/activate to start the enviroment ($ deactivate to stop it)
   now you can install whatever you want (Python stuff) and it doesnt affect your system
4. $ pip install Flask Flask-WTF Flask-SQLAlchemy
5. copy the rrvstool/ folder into the virtualenvironment folder

B) Setup the database
1. Create a new database in PostgreSQL >9.1 and run rrvstool_db.sql
2. Populate the database tables


MODIFYING DATAENTRY FORM
------------------------

A short step-by-step guideline on how to add a new QuerySelectField to the dataentry form:

1. models.py: 
#define a new column in the db model
mat_type = db.Column(db.String(254))

2. forms.py: 
#define a new field in the form
mat_type_field = QuerySelectField("Material Type", query_factory=getMatType, get_label='description', allow_blank=True)
			 
#add a new query factory which fills the dropdown menu
def getMatType(): 
	return dic_attribute_value.query.filter_by(attribute_type_code='MAT_TYPE') 

3. rrvsform.html: 
#add the new field to the html template
{{ rrvs_form.mat_type_field.label }}
{{ rrvs_form.mat_type_field }}
			 
#add new return value from .getJSON function
$('select[name="mat_type_field"]').val(data.mat_type_gid);

4. routes.py:
#in update_rrvsform() define the query attribute_value for the select fields
mat_type_val = ve_resolution1.query.filter_by(gid=gid_val).first().mat_type

# and the return gid
mat_type_gid = dic_attribute_value.query.filter_by(attribute_value=mat_type_val).first().gid,

#in rrvsform() add a new entry to the row.update() function to update database with form content
ve_resolution1.mat_type: rrvs_form.mat_type_field.data.attribute_value,
