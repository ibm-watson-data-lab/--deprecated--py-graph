import os

from dotenv import load_dotenv
from ibm_graph import IBMGraphClient


def test_create_graph():
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
    graph_client = IBMGraphClient(
        os.environ.get("TEST_API_URL"),
        os.environ.get("TEST_USERNAME"),
        os.environ.get("TEST_PASSWORD")
    )
    # create new graph
    #graph_id = graph_client.create_graph()
    #assert graph_id is not None
    # verify graph exists
    print "hello there"
    graph_ids = graph_client.get_graphs()
    print graph_ids
    #assert graph_id in graph_ids
    # delete graph
    #graph_client.delete_graph(graph_id)
    # verify graph no longer exists
    #graph_ids = graph_client.get_graphs()
    #assert graph_id not in graph_ids
