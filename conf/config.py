import configparser
import os


class HelixaAppConfiguration:
    config_parser = configparser.ConfigParser(os.environ)
    app_conf_path = os.environ["HELIXA_APP_CONFIG"]
    config_parser.read(app_conf_path)

    # Basic Flask Configuration values
    FLASK_ENV = config_parser.get('app', 'env')
    ENV = config_parser.get('app', 'env')
    DEBUG = config_parser.get("app", "debug")
    TESTING = config_parser.get("app", "testing")
    LOG_CONF = config_parser.get("logging", "log_conf_path")
