from flask import Flask
from flask_bootstrap import Bootstrap
from filters import date_timeformat, file_type
from S3config import S3

from . import buckets
from . import files

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    Bootstrap(app)

    # Setup Jinja Filters to Map to Custom Python Functions
    # These functions will
    app.jinja_env.filters['Hdatetimeformat'] = date_timeformat
    app.jinja_env.filters['file_type'] = file_type


    # Register the Blueprints
    app.register_blueprint(buckets.bp)
    app.register_blueprint(files.bp)

    # First Get all the Keys From the Config File
    s3config = S3.get_config()
    app.secret_key = s3config.APP_SECRET_KEY

    return app

#
# if __name__== '__main__':
#     print('Launching App')
#     app.run(host="127.0.0.1",port="6000")




