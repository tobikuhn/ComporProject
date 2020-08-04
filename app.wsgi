import logging
import os
import sys

sys.path.insert(0, '/var/www/compor-plus/')

os.environ['FLASK_ENV'] = "development"

logging.basicConfig(stream=sys.stderr)

from app import create_app

application = create_app()
