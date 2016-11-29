import pytest

from ibm_graph import Vertex


@pytest.fixture(scope='session')
@pytest.mark.usefixtures('graph_client', 'graph_id', 'graph_schema')
def graph_vertices(graph_client):
    create_update_john_doe_vertex(graph_client)
    create_jane_doe_vertex(graph_client)
    pass


def create_update_john_doe_vertex(graph_client):
    print("Creating John Doe vertex.")
    # create vertex
    original_vertex = Vertex('person', {'name': 'John Doe', 'country': 'United States'})
    added_vertex = graph_client.add_vertex(original_vertex)
    assert added_vertex is not None
    assert added_vertex.get_property_value('name') == original_vertex.get_property_value('name')
    assert added_vertex.get_property_value('country') == original_vertex.get_property_value('country')
    # get vertex
    vertex = graph_client.get_vertex(added_vertex.id)
    assert vertex is not None
    assert vertex.id == added_vertex.id
    assert vertex.get_property_value('name') == added_vertex.get_property_value('name')
    assert vertex.get_property_value('country') == added_vertex.get_property_value('country')
    # update vertex
    vertex.set_property_value('country', 'Canada')
    updated_vertex = graph_client.update_vertex(vertex)
    assert updated_vertex is not None
    assert updated_vertex.get_property_value('name') == vertex.get_property_value('name')
    # query vertex again to verify
    vertex = graph_client.get_vertex(updated_vertex.id)
    assert vertex is not None
    assert vertex.get_property_value('name') == updated_vertex.get_property_value('name')
    assert vertex.get_property_value('country') == updated_vertex.get_property_value('country')


def create_jane_doe_vertex(graph_client):
    print("Creating Jane Doe vertex.")
    # create vertex
    original_vertex = Vertex('person', {'name':'Jane Doe', 'country':'United States'})
    added_vertex = graph_client.add_vertex(original_vertex)
    assert added_vertex is not None
    assert added_vertex.get_property_value('name') == original_vertex.get_property_value('name')
    assert added_vertex.get_property_value('country') == original_vertex.get_property_value('country')


@pytest.mark.usefixtures('graph_client', 'graph_id', 'graph_schema')
def test_create_delete_empty_vertex(graph_client):
    print("Executing test_create_delete_empty_vertex.")
    # create vertex
    added_vertex = graph_client.add_vertex()
    assert added_vertex is not None
    # query vertex
    vertex = graph_client.get_vertex(added_vertex.id)
    assert vertex is not None
    assert vertex.id == added_vertex.id
    # delete vertex
    deleted = graph_client.delete_vertex(vertex.id)
    assert deleted
    # make sure vertex is gone
    vertex = graph_client.get_vertex(added_vertex.id)
    assert vertex is None
