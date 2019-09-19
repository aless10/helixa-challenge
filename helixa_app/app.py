import logging

from conf.config import HelixaAppConfiguration
from helixa_app.app_factory import create_app

log = logging.getLogger(__name__)

helixa_app = create_app(HelixaAppConfiguration)
log.debug("Starting the Helixa Application with config: %s", helixa_app.config)

if __name__ == '__main__':
    helixa_app.run()
