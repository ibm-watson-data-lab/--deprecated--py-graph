class EdgeLabel(dict):

    def __init__(self, name, multiplicity='SIMPLE'):
        self.name = name
        self.multiplicity = multiplicity
        self['name'] = name
        self['multiplicity'] = multiplicity

    @staticmethod
    def from_json_object(json_object):
        return EdgeLabel(json_object['name'], json_object['multiplicity'])
