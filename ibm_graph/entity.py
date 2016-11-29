from .element import Element


class Entity(Element):

    def __init__(self, label, properties=None):
        self.label = label
        if properties is None:
            self.properties = {}
        else:
            self.properties = properties
        self['label'] = label
        self['properties'] = properties

    def set_id(self, id):
        self.id = id
        self['id'] = id

    def set_properties(self, json_properties):
        self.properties = {}
        if json_properties is not None:
            for key in json_properties.keys():
                name = str(key)
                o = json_properties[name]
                if isinstance(o, list):
                    value = o[0]['value']
                elif isinstance(o, dict) and 'value' in o.keys():
                    value = o['value']
                else:
                    value = o
                self.set_property_value(name, value)
        self['properties'] = self.properties

    def get_property_value(self, property_name):
        if self.properties is not None and property_name in self.properties.keys():
            return self.properties[property_name]
        else:
            return None

    def set_property_value(self, name, value):
        self.properties[name] = value

    @staticmethod
    def from_json_object(json_object):
        from .edge import Edge
        from .vertex import Vertex
        if json_object['type'].lower() == 'edge':
            return Edge.from_json_object(json_object)
        else:
            return Vertex.from_json_object(json_object)
