import os
from unittest import mock
import pytest

import main

@pytest.fixture
def client():
    main.app.testing = True
    return main.app.test_client()

def test_index(client):
    r = client.get('/')
    assert r.status_code == 200