# Experimental Python Client for IBM Graph

This is an Experimental Python library for working with IBM Graph.

[![Build Status](https://travis-ci.org/ibm-cds-labs/py-graph.svg?branch=master)](https://travis-ci.org/ibm-cds-labs/py-graph)

Use with caution!

Currently the library supports:
 
 - Running Gremlin queries
 - Adding/deleting graphs
 - Adding/updating/deleting vertices
 - Adding/updating/deleting edges
 - Creating/updating schema
 - Deleting indexes

# How to Install

```
git clone https://github.com/ibm-cds-labs/py-graph

pip install -e <path_to_py_graph>
```

# How to Run (Dictionary API)

```
from ibm_graph import IBMGraphClient

api_url = 'https://ibmgraph-alpha.ng.bluemix.net/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/g'
username = ''
password = ''
graph_client = IBMGraphClient(api_url, username, password)

graph_client.save_schema({
    'propertyKeys': [
        {'name': 'name', 'dataType': 'String', 'cardinality': 'SINGLE'}
    ],
    'vertexLabels': [
        {'name': 'person'}
    ]
    'edgeLabels': [
        {'name': 'friend'}
    ],
    'vertexIndexes': [
        {'name': 'vertexByName', 'propertyKeys': ['name'], 'composite': True, 'unique': True}
    ],
    'edgeIndexes': []
})

graph_client.add_vertex({
    'label': 'person',
    'properties': {
        'name': 'John'
    }
})

graph_client.add_edge({
    'label': 'friend',
    'outV': out_v_id,
    'inV': in_v_id,
    'properties': {
        'date': d
    }
})
```

# How to Run (Object API)

```
from ibm_graph import IBMGraphClient

api_url = 'https://ibmgraph-alpha.ng.bluemix.net/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/g'
username = ''
password = ''
graph_client = IBMGraphClient(api_url, username, password)

schema = Schema(
    [PropertyKey('name', 'String', 'SINGLE')],
    [VertexLabel('person')],
    [EdgeLabel('friend')],
    [VertexIndex('vertexByName', ['name'], True, True)],
    []
)
schema = graph_client.save_schema(schema)

vertex = Vertex('person', {
    'name': 'John'
})
vertex = graph_client.add_vertex(vertex)

edge = Edge('friend', out_v_id, in_v_id, {
   'date': d
})
edge = graph_client.add_edge(edge)
```

Work in progress!
