class Element(dict):

    @staticmethod
    def from_json_object(json_object):
        from .entity import Entity
        from .path import Path
        if 'objects' in json_object.keys():
            return Path.from_json_object(json_object)
        else:
            return Entity.from_json_object(json_object)
