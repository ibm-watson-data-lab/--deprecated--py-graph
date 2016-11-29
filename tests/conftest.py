import os
import pytest
import uuid

from dotenv import load_dotenv
from ibm_graph import IBMGraphClient


@pytest.fixture(scope="module")
def graph_client():
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
    return IBMGraphClient(
        os.environ.get("TEST_API_URL"),
        os.environ.get("TEST_USERNAME"),
        os.environ.get("TEST_PASSWORD")
    )


@pytest.fixture(scope="module")
def graph_id(graph_client):
    g_id = str(uuid.uuid4())
    graph_client.create_graph(g_id)
    graph_client.set_graph(g_id)
    yield g_id
    print("Deleting Graph with ID {}".format(g_id))
    graph_client.delete_graph(g_id)
