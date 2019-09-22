from helixa_app.conf.config import HelixaAppConfiguration
from helixa_app.app_factory import create_app, run_app


helixa_app = create_app(HelixaAppConfiguration)

if __name__ == '__main__':
    run_app(helixa_app)
