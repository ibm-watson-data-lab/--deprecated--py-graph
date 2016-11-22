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
            o = self.properties[property_name]
            if isinstance(o, list):
                return list[0]['value']
            elif isinstance(o, dict) and 'value' in o.keys():
                return list['value']
            else:
                return o

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
