import base64
import httplib
import json


class IBMGraphClient(object):

    def __init__(self, api_url, username, password):
        self.api_url = api_url
        self.username = username
        self.password = password
        self.gds_token_auth = None
        self.query_prefix = 'def g = graph.traversal(); '
        self.basic_auth_header = 'Basic {}'.format(base64.b64encode('{}:{}'.format(self.username, self.password)))
        url = self.api_url
        index = self.api_url.find('://')
        if index > 0:
            url = self.api_url[self.api_url.find('://')+3:]
        self.base_url = url[0:url.find('/')]
        self.base_path_prefix = url[url.find('/'):url.rfind('/')]
        self.api_path_prefix = url[url.find('/'):]

    def init_session(self):
        conn = httplib.HTTPSConnection(self.base_url)
        conn.request("GET", '{}/_session'.format(self.base_path_prefix), headers={
            'Authorization': self.basic_auth_header
        })
        response = conn.getresponse()
        data = response.read()
        token = str(json.loads(data)['gds-token'])
        self.gds_token_auth = 'gds-token {}'.format(token)
        conn.close()

    def get_schema(self):
        response = self.do_http_get('/schema')
        return response['result']['data'][0]

    def save_schema(self, schema):
        path = '/schema'
        response = self.do_http_post(path, json.dumps(schema))
        data = response['result']['data']
        if len(data) > 0:
            return data[0]
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
            return data[0]
        else:
            return None

    def update_vertex(self, vertex):
        path = '/vertices/{}'.format(vertex['id'])
        response = self.do_http_post(path, json.dumps(vertex))
        data = response['result']['data']
        if len(data) > 0:
            return data[0]
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
            return data[0]
        else:
            return None

    def update_edge(self, edge):
        path = '/edges/{}'.format(edge['id'])
        response = self.do_http_post(path, json.dumps(edge))
        data = response['result']['data']
        if len(data) > 0:
            return data[0]
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
        return response['result']['data']

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
        if self.gds_token_auth is None:
            self.init_session()
        conn = httplib.HTTPSConnection(self.base_url)
        conn.request('GET', '{}{}'.format(self.api_path_prefix, path), headers={
            'Authorization': self.gds_token_auth,
            'Accept': 'application/json'
        })
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return json.loads(data)

    def do_http_post(self, path, body):
        if self.gds_token_auth is None:
            self.init_session()
        conn = httplib.HTTPSConnection(self.base_url)
        conn.request('POST', '{}{}'.format(self.api_path_prefix, path), body, headers={
            'Authorization': self.gds_token_auth,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return json.loads(data)

    def do_http_put(self, path, body):
        if self.gds_token_auth is None:
            self.init_session()
        conn = httplib.HTTPSConnection(self.base_url)
        conn.request('PUT', '{}{}'.format(self.api_path_prefix, path), body, headers={
            'Authorization': self.gds_token_auth,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return json.loads(data)

    def do_http_delete(self, path):
        if self.gds_token_auth is None:
            self.init_session()
        conn = httplib.HTTPSConnection(self.base_url)
        conn.request('POST', '{}{}'.format(self.api_path_prefix, path), headers={
            'Authorization': self.gds_token_auth,
            'Accept': 'application/json'
        })
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return json.loads(data)
