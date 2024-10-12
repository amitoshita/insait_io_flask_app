import pytest
from unittest.mock import Mock
from app import create_app, db
from app.config import TestConfig  # Import the TestConfig class
from app.models import QuestionAnswer

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app(config_class=TestConfig)  # Use TestConfig here
    with app.app_context():
        db.create_all()  # Create tables
        yield app
        db.session.remove()
        db.drop_all()  # Drop tables after the test

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_ask_question(client, mocker):
    """Test the /ask endpoint with a mocked OpenAI API."""
    question = "What is the the colors of israel's flag?"
    mocked_answer = "The colors of the flag of Israel are blue and white"

    # Create a mock response object
    mock_response = Mock()
    mock_response.choices = [Mock(message={'content': mocked_answer})]

    # Patch the OpenAI API call to return the mock response
    mocker.patch('openai.ChatCompletion.create', return_value=mock_response)

    # Send POST request to /ask
    response = client.post('/ask', json={'question': question})

    assert response.status_code == 200

    data = response.get_json()
    assert data['question'] == question
    assert data['answer'] == mocked_answer

    qa = QuestionAnswer.query.first()
    assert qa is not None
    assert qa.question == question
    assert qa.answer == mocked_answer
