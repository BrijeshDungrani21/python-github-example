from app import app

def test_index():
    # Create a test client
    client = app.test_client()

    # Use the test client to simulate a request to the '/' route
    response = client.get('/')

    # Check if the response data is as expected
    assert response.data.decode('utf-8') == "Hello world!"