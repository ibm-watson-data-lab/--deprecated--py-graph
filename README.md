# Experimental Python Client for IBM Graph

This is an Experimental Python library for working with IBM Graph.

Use with caution!

Currently the library supports:
 
 - Running Gremlin queries
 - Adding/updating/deleting vertices
 - Adding/updating/deleting edges
 - Creating/updating schema
 - Deleting indexes

# How to Install

```
git clone https://github.com/ibm-cds-labs/py-graph

pip install -e <path_to_py_graph>
```

# How to Run

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
    'label': 'selects',
    'outV': out_v_id,
    'inV': in_v_id,
    'properties': {
        'date': d
    }
})
```

Work in progress!
