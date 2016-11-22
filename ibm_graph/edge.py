from .entity import Entity


class Edge(Entity):

    def __init__(self, label, out_v, in_v, properties=None):
        super(Edge, self).__init__(label, properties)
        self.out_v = out_v
        self.in_v = in_v
        self['outV'] = out_v
        self['inV'] = in_v

    @staticmethod
    def from_json_object(json_object):
        edge = Edge(json_object['label'], json_object['outV'], json_object['inV'], json_object['properties'])
        edge.id = json_object['id']
        edge.out_v_label = json_object['outVLabel']
        edge.in_v_label = json_object['inVLabel']
        edge['id'] = edge.id
        edge['outVLabel'] = edge.out_v_label
        edge['inVLabel'] = edge.in_v_label
        return edge
