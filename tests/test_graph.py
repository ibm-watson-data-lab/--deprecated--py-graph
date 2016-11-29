import pytest


@pytest.mark.usefixtures('graph_client')
def test_create_graph(graph_client):
    # create new graph
    graph_id = graph_client.create_graph()
    assert graph_id is not None
    # verify graph exists
    graph_ids = graph_client.get_graphs()
    assert graph_id in graph_ids
    # delete graph
    graph_client.delete_graph(graph_id)
    # verify graph no longer exists
    graph_ids = graph_client.get_graphs()
    assert graph_id not in graph_ids