from flask.blueprints import Blueprint
from app import application

application.config.from_object('config')

mod_home = Blueprint("home_mod", __name__)


@mod_home.route('/', methods=["GET"])
def index():
    try:
        return 'Hi there, This is R-CNN Pneumonia'
    except Exception as e:
        return 'Hi Error Index'
