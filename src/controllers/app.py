from flask import Flask
from flask_cors import *
from .env import Env
from ..classes.route_class import Route

class App:
    def __init__(self, env: Env, routes: list[tuple[Route, any]] = None):
        self.env = env
        self.app = Flask(env.config.flask.name)
        self.__setup_routes__(routes) 
        self.__setup_cors__()
    
    def __call__(self, *args, **kwargs):
        return self.app(*args, **kwargs)
    
    def __setup_cors__(self):
        CORS(self.app)
        
    def __setup_routes__(self, routes: list[tuple[Route, any]]):
        for route in routes: 
            setattr(App, route[0].name, route[1])
            self.app.add_url_rule(route[0].path, route[0].name, getattr(self, route[0].name), methods=route[0].method)

    def run(self):
        self.app.run(
            host = self.env.config.flask.host,
            port = int(self.env.config.flask.port),
            debug = bool(self.env.config.flask.debug),
        )