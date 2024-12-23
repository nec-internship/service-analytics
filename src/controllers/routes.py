from classes.route_class import Route
METHOD_HEAD = ['HEAD']
METHOD_GET = ['GET']
METHOD_POST = ['POST']
METHOD_PUT = ['PUT']
METHOD_DELETE = ['DELETE']
METHOD_PATCH = ['PATCH']

ROUTE_PING = Route(
    name='ping',
    path='/ping',
    method=METHOD_GET
)
