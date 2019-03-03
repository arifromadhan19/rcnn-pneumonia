from app import application
from app.mod.mod_home.controller import mod_home

application.register_blueprint(mod_home)