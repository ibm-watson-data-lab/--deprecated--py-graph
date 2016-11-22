from .edge_index import EdgeIndex
from .edge_label import EdgeLabel
from .property_key import PropertyKey
from .vertex_index import VertexIndex
from .vertex_label import VertexLabel


class Schema(dict):

    def __init__(self, property_keys, vertex_labels, edge_labels, vertex_indexes, edge_indexes):
        self.property_keys = property_keys
        self.vertex_labels = vertex_labels
        self.edge_labels = edge_labels
        self.vertex_indexes = vertex_indexes
        self.edge_indexes = edge_indexes
        self['propertyKeys'] = property_keys
        self['vertexLabels'] = vertex_labels
        self['edgeLabels'] = edge_labels
        self['vertexIndexes'] = vertex_indexes
        self['edgeIndexes'] = edge_indexes

    @staticmethod
    def from_json_object(json_object):
        property_keys = []
        vertex_labels = []
        edge_labels = []
        vertex_indexes = []
        edge_indexes = []
        if 'propertyKeys' in json_object.keys():
            for property_key in json_object['propertyKeys']:
                property_keys.append(PropertyKey.from_json_object(property_key))
        if 'vertexLabels' in json_object.keys():
            for vertex_label in json_object['vertexLabels']:
                vertex_labels.append(VertexLabel.from_json_object(vertex_label))
        if 'edgeLabels' in json_object.keys():
            for edge_label in json_object['edgeLabels']:
                edge_labels.append(EdgeLabel.from_json_object(edge_label))
        if 'vertexIndexes' in json_object.keys():
            for vertex_index in json_object['vertexIndexes']:
                vertex_indexes.append(VertexIndex.from_json_object(vertex_index))
        if 'edgeIndexes' in json_object.keys():
            for edge_index in json_object['edgeIndexes']:
                edge_indexes.append(EdgeIndex.from_json_object(edge_index))
        return Schema(property_keys, vertex_labels, edge_labels, vertex_indexes, edge_indexes)
