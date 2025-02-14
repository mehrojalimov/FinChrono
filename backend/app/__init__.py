# Initialize Flask app
from flask import Flask
from .config import Config  # Import any configuration you need
from .models import db  # Import SQLAlchemy if you're using it
from .tasks import celery  # Import Celery instance if needed

# Initialize the app
app = Flask(__name__)
app.config.from_object(Config)  # Configure the app using the config class

# Initialize db and celery with the app
db.init_app(app)
celery.conf.update(app.config)
