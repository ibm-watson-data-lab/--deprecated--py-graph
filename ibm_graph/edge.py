from .entity import Entity


class Edge(Entity):

    def __init__(self, label, out_v, in_v, properties=None):
        super(Edge, self).__init__(label, properties)
        self.out_v = out_v
        self.in_v = in_v
        self['outV'] = self.out_v
        self['inV'] = self.in_v

    @staticmethod
    def from_json_object(json_object):
        edge = Edge(json_object['label'], json_object['outV'], json_object['inV'])
        edge.set_id(json_object['id'])
        if 'properties' in edge.keys():
            edge.set_properties(json_object['properties'])
        edge.out_v_label = json_object['outVLabel']
        edge.in_v_label = json_object['inVLabel']
        edge['outVLabel'] = edge.out_v_label
        edge['inVLabel'] = edge.in_v_label
        return edge
