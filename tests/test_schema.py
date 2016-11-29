import pytest

from ibm_graph.schema import EdgeIndex
from ibm_graph.schema import EdgeLabel
from ibm_graph.schema import PropertyKey
from ibm_graph.schema import Schema
from ibm_graph.schema import VertexIndex
from ibm_graph.schema import VertexLabel


# this just forces this test to run prior to other tests that depend on it
@pytest.fixture(scope='session')
@pytest.mark.usefixtures('graph_client', 'graph_id')
def graph_schema(graph_client):
    create_schema(graph_client)


def create_schema(graph_client):
    print ("Creating schema.")
    # create new graph
    schema = graph_client.get_schema()
    schema_exists = (schema is not None and schema.property_keys is not None and len(schema.property_keys) > 0)
    assert not schema_exists
    # crete new schema
    schema = Schema(
        [
            PropertyKey('name', 'String', 'SINGLE'),
            PropertyKey('country', 'String', 'SINGLE'),
            PropertyKey('date', 'Integer', 'SINGLE'),
        ],
        [
            VertexLabel('person')
        ],
        [
            EdgeLabel('friends', 'SIMPLE')
        ],
        [
            VertexIndex('vertexByName', ['name'], True, True)
        ],
        [
            EdgeIndex('edgeByDate', ['date'], True, False)
        ]
    )
    schema = graph_client.save_schema(schema)
    assert schema is not None
