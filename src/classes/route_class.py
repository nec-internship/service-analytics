class Route: 
    def __init__(self, name, path, method):
        self.name = name
        self.path = path
        self.method = method 
        
METHOD_HEAD = ['HEAD']
METHOD_GET = ['GET']
METHOD_POST = ['POST']
METHOD_PUT = ['PUT']
METHOD_DELETE = ['DELETE']
METHOD_PATCH = ['PATCH']