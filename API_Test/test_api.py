import pytest
import requests
import json
import os
# Base URL for the API
BASE_URL = 'http://localhost:5000/api/tasks'

@pytest.fixture
def load_json_data():
    """
    Fixture to load data from the JSON file.
    """
    json_file_path = 'task_data.json'
    with open(json_file_path, 'r') as file:
        data = json.load(file)  # Load JSON data
    return data


@pytest.fixture
def setup_task(load_json_data):
    """
    Fixture to create a task before the tests and clean it up afterward.
    """
    # Pre-test: Create a task using data from the JSON file
    task_data = load_json_data
    response = requests.post(BASE_URL, json=task_data)
    assert response.status_code == 201  # Task created successfully

    # Provide the task details for the tests
    task = response.json()
    yield task

    # Post-test: Cleanup by deleting the task
    requests.delete(f"{BASE_URL}/{task['id']}")


def test_create_task(load_json_data):
    """
    Test for creating a task using JSON data.
    """
    task_data = load_json_data

    # Sending a POST request to create a new task using JSON data
    response = requests.post(BASE_URL, json=task_data)

    assert response.status_code == 201  # Check if the task was created successfully
    response_data = response.json()

    # Assertions to verify the response content matches the JSON data
    assert response_data['title'] == task_data['title']
    assert response_data['description'] == task_data['description']
    assert response_data['priority'] == task_data['priority']
    assert 'id' in response_data  # Ensure the task ID is returned


def test_get_task(setup_task):
    """
    Test for retrieving a task by its ID (using data created from JSON file).
    """
    task_id = setup_task['id']

    # Sending a GET request to fetch the task details
    response = requests.get(f"{BASE_URL}/{task_id}")

    assert response.status_code == 200  # Check if the task was retrieved successfully

    task_data = response.json()

    # Assertions to verify the retrieved task content
    assert task_data['title'] == setup_task['title']
    assert task_data['description'] == setup_task['description']
    assert task_data['priority'] == setup_task['priority']
