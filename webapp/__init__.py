from flask import Flask,request,session
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.security import Security,SQLAlchemyUserDatastore
from flask.ext.babel import Babel
from flask_kvsession import KVSessionExtension
import redis
from simplekv.memory.redisstore import RedisStore
from datetime import timedelta
from werkzeug.contrib.profiler import ProfilerMiddleware


store=RedisStore(redis.StrictRedis())

app = Flask(__name__)
app.config.from_object('rrvs_config')
app.config['PROFILE']=True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
app.permanent_session_lifetime = timedelta(hours=8)
KVSessionExtension(store, app)

db = SQLAlchemy(app)

import webapp.views
db.init_app(app)

babel = Babel(app)
#app.config['BABEL_DEFAULT_LOCALE'] = 'ar'

#create login_manager
login_manager = LoginManager()
login_manager.init_app(app)
#setup flask security
user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)

@babel.localeselector
def get_locale():
    lang = request.accept_languages.best_match(['ar','en'])
    session['lang']=lang
    return lang

@app.before_request
def func():
    session.modified = True

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/')


if __name__== "__main__":

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(int(user_id))
    @babel.localeselector
    def get_locale():
        #return request.accept_languages.best_match(['ar','en'])
       # return 'ar'
        lang = request.accept_languages.best_match(['ar','en'])
        session['lang']=lang
        return lang
    @app.before_request
    def func():
        session.modified = True

    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect('/')


    app.run(host="0.0.0.0")
