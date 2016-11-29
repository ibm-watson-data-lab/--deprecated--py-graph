def test_create_delete_empty_vertex(graph_client, graph_id):
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
