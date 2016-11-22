from .entity import Entity


class Vertex(Entity):

    def __init__(self, label, properties=None):
        super(Vertex, self).__init__(label, properties)

    @staticmethod
    def from_json_object(json_object):
        vertex = Vertex(json_object['label'], json_object['properties'])
        vertex.id = json_object['id']
        vertex['id'] = vertex.id
        return vertex
