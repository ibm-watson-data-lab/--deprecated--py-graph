import os
import pytest
import uuid

from dotenv import load_dotenv
from ibm_graph import IBMGraphClient
from .test_schema import graph_schema
from .test_vertex import graph_vertices


@pytest.fixture(scope='session')
def graph_client():
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
    return IBMGraphClient(
        os.environ.get("TEST_API_URL"),
        os.environ.get("TEST_USERNAME"),
        os.environ.get("TEST_PASSWORD")
    )


@pytest.fixture(scope='session')
@pytest.mark.usefixtures('graph_client')
def graph_id(graph_client):
    print("Creating Graph.")
    g_id = str(uuid.uuid4())
    graph_client.create_graph(g_id)
    graph_client.set_graph(g_id)
    yield g_id
    print("Deleting graph with ID {}".format(g_id))
    graph_client.delete_graph(g_id)