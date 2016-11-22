class EdgeLabel(dict):

    def __init__(self, name):
        self.name = name
        self['name'] = name

    @staticmethod
    def from_json_object(json_object):
        return EdgeLabel(json_object['name'])
