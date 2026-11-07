
from fastapi.testclient import TestClient
from app.main import app, tasks
import pytest

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_tasks():
    tasks.clear()
    yield
    tasks.clear()


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to TaskFlow API"
    }


def test_add_task():
    response = client.post(
        "/tasks",
        json={"title": "Complete DevOps assignment"}
    )

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["title"] == "Complete DevOps assignment"


def test_get_tasks():
    client.post(
        "/tasks",
        json={"title": "Learn Docker"}
    )

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_task_count():
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})

    response = client.get("/tasks/count")

    assert response.status_code == 200
    assert response.json()["total_tasks"] == 2
