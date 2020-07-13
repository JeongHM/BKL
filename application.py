import os

import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(import_name=__name__)
    app.secret_key = os.urandom(16)

    logger = logging.getLogger(name=__name__)
    logger.setLevel(level=logging.INFO)
    logger_format = '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
    logger_formatter = logging.Formatter(fmt=logger_format)
    logger_handler = RotatingFileHandler(filename='./application.log',
                                         mode='a',
                                         maxBytes=1024 * 1024 * 8,
                                         backupCount=5,
                                         encoding='utf-8')
    logger_handler.setFormatter(fmt=logger_formatter)
    app.logger.addHandler(hdlr=logger_handler)

    from controllers.users import users_blueprint
    app.register_blueprint(blueprint=users_blueprint, url_prefix='/users')

    CORS(app=app)

    return app


application = create_app()


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5050, debug=False)