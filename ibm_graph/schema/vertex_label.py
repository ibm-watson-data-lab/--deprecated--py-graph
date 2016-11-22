class VertexLabel(dict):

    def __init__(self, name):
        self.name = name
        self['name'] = name

    @staticmethod
    def from_json_object(json_object):
        return VertexLabel(json_object['name'])
