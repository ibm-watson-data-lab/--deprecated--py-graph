class PropertyKey(dict):

    def __init__(self, name, data_type, cardinality):
        self.name = name
        self.data_type = data_type
        self.cardinality = cardinality
        self['name'] = name
        self['dataType'] = data_type
        self['cardinality'] = cardinality

    @staticmethod
    def from_json_object(json_object):
        return PropertyKey(
            json_object['name'],
            json_object['dataType'],
            json_object['cardinality']
        )
