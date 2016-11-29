import pytest
import time

from ibm_graph import Edge


@pytest.mark.usefixtures('graph_client', 'graph_id', 'graph_schema', 'graph_vertices')
def test_create_delete_edge(graph_client):
    print("Executing test_create_delete_edge.")
    # find jane and john doe
    # and create edge from jane doe to john doe
    jane_doe_vertex = graph_client.run_gremlin_query('g.V().hasLabel("person").has("name", "Jane Doe")')[0];
    john_doe_vertex = graph_client.run_gremlin_query('g.V().hasLabel("person").has("name", "John Doe")')[0];
    original_edge = Edge('friends', jane_doe_vertex.id, john_doe_vertex.id, {
        'date': int(time.time())
    })
    added_edge = graph_client.add_edge(original_edge);
    assert added_edge is not None
