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

    def get_property_value(self, property_name):
        if property_name not in self.properties.keys():
            return None
        else:
            prop = self.properties[property_name]
            if isinstance(prop, list):
                return prop[0]['value']
            elif isinstance(prop, dict) and 'value' in prop.keys():
                return prop['value']
            else:
                return prop

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
