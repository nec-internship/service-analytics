import os
import sys
sys.path.append(os.curdir)
from src.controllers.app import App, Env
from src.controllers.apis import *
from gunicorn.app.base import BaseApplication
app = App(env = Env(), routes=APIS)

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
class WSGIApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application
    
if __name__ == "__main__":
    # Init wsgi application 
    app_config = app.env.config
    wsgi_options = {
        "bind": f"{app_config.flask.host}:{app_config.flask.port}",
        "workers": 1,
        "reload": app_config.flask.debug,
        "log-level": "WARNING",
        "timeout": 120
    }
    wsgi_app = WSGIApplication(app=app, options=wsgi_options)
    wsgi_app.run()