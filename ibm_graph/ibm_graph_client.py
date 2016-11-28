import base64
import httplib
import json

from .edge import Edge
from .element import Element
from .vertex import Vertex
from .schema.schema import Schema


class IBMGraphClient(object):

    def __init__(self, api_url, username, password):
        self.api_url = api_url
        self.username = username
        self.password = password
        self.gds_token_auth = None
        url = self.api_url
        index = self.api_url.find('://')
        if index > 0:
            url = self.api_url[self.api_url.find('://')+3:]
        self.base_url = url[0:url.find('/')]
        self.base_path_prefix = url[url.find('/'):url.rfind('/')]
        self.api_path_prefix = url[url.find('/'):]

    def init_session(self):
        basic_auth_header = 'Basic {}'.format(base64.b64encode('{}:{}'.format(self.username, self.password)))
        conn = httplib.HTTPSConnection(self.base_url)
        conn.request("GET", '{}/_session'.format(self.base_path_prefix), headers={
            'Authorization': basic_auth_header
        })
        response = conn.getresponse()
        data = response.read()
        token = str(json.loads(data)['gds-token'])
        self.gds_token_auth = 'gds-token {}'.format(token)
        conn.close()

    # Graphs

    def get_graphs(self):
        response = self.do_http_get_url('{}/_graphs'.format(self.base_path_prefix))
        return response['graphs']

    def create_graph(self, graph_id=None):
        url = '{}/_graphs'.format(self.base_path_prefix)
        if graph_id is not None:
            url += '/{}'.format(graph_id)
        response = self.do_http_post_url(url)
        return response['graphId']

    def delete_graph(self, graph_id):
        url = '{}/_graphs/{}'.format(self.base_path_prefix, graph_id)
        self.do_http_delete_url(url)

    # Schema
    
    def get_schema(self):
        response = self.do_http_get('/schema')
        return Schema.from_json_object(response['result']['data'][0])

    def save_schema(self, schema):
        path = '/schema'
        response = self.do_http_post(path, json.dumps(schema))
        data = response['result']['data']
        if len(data) > 0:
            return Schema.from_json_object(data[0])
        else:
            return None

    def delete_index(self, index_name):
        path = '/index/{}'.format(index_name)
        response = self.do_http_delete(path)
        data = response['result']['data']
        if len(data) > 0:
            return data[0]
        else:
            return None

    # Vertices

    def add_vertex(self, vertex):
        path = '/vertices'
        response = self.do_http_post(path, json.dumps(vertex))
        data = response['result']['data']
        if len(data) > 0:
            return Vertex.from_json_object(data[0])
        else:
            return None

    def update_vertex(self, vertex):
        path = '/vertices/{}'.format(vertex['id'])
        response = self.do_http_post(path, json.dumps(vertex))
        data = response['result']['data']
        if len(data) > 0:
            return Vertex.from_json_object(data[0])
        else:
            return None

    def delete_vertex(self, vertex_id):
        path = '/vertices/{}'.format(vertex_id)
        response = self.do_http_delete(path)
        data = response['result']['data']
        if len(data) > 0:
            return data[0]
        else:
            return None

    # Edges

    def add_edge(self, edge):
        path = '/edges'
        response = self.do_http_post(path, json.dumps(edge))
        data = response['result']['data']
        if len(data) > 0:
            return Edge.from_json_object(data[0])
        else:
            return None

    def update_edge(self, edge):
        path = '/edges/{}'.format(edge['id'])
        response = self.do_http_post(path, json.dumps(edge))
        data = response['result']['data']
        if len(data) > 0:
            return Edge.from_json_object(data[0])
        else:
            return None

    def delete_edge(self, edge_id):
        path = '/edges/{}'.format(edge_id)
        response = self.do_http_delete(path)
        data = response['result']['data']
        if len(data) > 0:
            return data[0]
        else:
            return None

    # Gremlin

    def run_gremlin_query(self, query):
        path = '/gremlin'
        body = {
            'gremlin': 'def g = graph.traversal(); {}'.format(query)
        }
        response = self.do_http_post(path, json.dumps(body))
        json_array = response['result']['data']
        elements = []
        if len(json_array) > 0:
            for json_object in json_array:
                elements.append(Element.from_json_object(json_object))
        return elements


    # def bulkload_graphson(self):
    #     resp = self.do_http_post(
    #         '/bulkload/graphson',
    #         file_path='./data/nxnw_dataset_v3.json'
    #     )
    #     if resp is not None and 'result' in resp:
    #         self.logger.info(resp['result'])

    # def bulkload_graphson(self, filepath):
    #     resp = self.do_http_post(
    #         '/bulkload/graphson',
    #         file_path=filepath
    #     )
    #     if resp is not None and 'result' in resp:
    #         self.logger.info(resp['result'])

    # HTTP Helper Methods

    def do_http_get(self, path):
        return self.do_http_get_url('{}{}'.format(self.api_path_prefix, path))

    def do_http_get_url(self, url):
        if self.gds_token_auth is None:
            self.init_session()
        conn = httplib.HTTPSConnection(self.base_url)
        conn.request('GET', url, headers={
            'Authorization': self.gds_token_auth,
            'Accept': 'application/json'
        })
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return json.loads(data)

    def do_http_post(self, path, body=None):
        return self.do_http_post_url('{}{}'.format(self.api_path_prefix, path), body)
        
    def do_http_post_url(self, url, body=None):
        if self.gds_token_auth is None:
            self.init_session()
        conn = httplib.HTTPSConnection(self.base_url)
        conn.request('POST', url, body, headers={
            'Authorization': self.gds_token_auth,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return json.loads(data)

    def do_http_put(self, path, body=None):
        return self.do_http_put_url('{}{}'.format(self.api_path_prefix, path), body)

    def do_http_put_url(self, url, body=None):
        if self.gds_token_auth is None:
            self.init_session()
        conn = httplib.HTTPSConnection(self.base_url)
        conn.request('PUT', url, body, headers={
            'Authorization': self.gds_token_auth,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return json.loads(data)

    def do_http_delete(self, path):
        return self.do_http_delete_url('{}{}'.format(self.api_path_prefix, path))

    def do_http_delete_url(self, url):
        if self.gds_token_auth is None:
            self.init_session()
        conn = httplib.HTTPSConnection(self.base_url)
        conn.request('DELETE', url, headers={
            'Authorization': self.gds_token_auth,
            'Accept': 'application/json'
        })
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return json.loads(data)
