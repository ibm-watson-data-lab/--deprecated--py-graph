class EdgeIndex(dict):

    def __init__(self, name, property_keys, composite, unique):
        self.name = name
        self.property_keys = property_keys
        self.composite = composite
        self.unique = unique
        self['name'] = name
        self['propertyKeys'] = property_keys
        self['composite'] = composite
        self['unique'] = unique

    @staticmethod
    def from_json_object(json_object):
        return EdgeIndex(
            json_object['name'],
            json_object['propertyKeys'],
            json_object['composite'],
            json_object['unique']
        )
