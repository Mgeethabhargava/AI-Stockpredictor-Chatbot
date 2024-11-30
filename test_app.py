# test_app.py
import pytest
from app import app  # Import your Flask app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test the homepage route."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Welcome to My Flask App' in rv.data  # Replace with your app's response text
