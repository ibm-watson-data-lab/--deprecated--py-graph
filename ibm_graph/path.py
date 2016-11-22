from .element import Element
from .entity import Entity


class Path(Element):

    def __init__(self, objects, labels):
        self.objects = objects
        self.labels = labels
        self['objects'] = objects
        self['labels'] = labels

    @staticmethod
    def from_json_object(json_object):
        objects = []
        json_objects = json_object['objects']
        for obj in json_objects:
            objects.append(Entity.from_json_object(obj))
        return Path(objects, json_object['labels'])
