# tests/test_e2e/test_e2e.py
"""
E2E: proste sprawdzenie CRUD na /tasks.
Używa Playwright APIRequestContext (bez otwierania przeglądarki).
"""

import json
import os
import pytest
from playwright.sync_api import sync_playwright, APIRequestContext

# Pozwala nadpisać adres w CI: BASE_URL=http://127.0.0.1:5000
BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:5000")


@pytest.fixture(scope="session")
def pw():
    """Jeden kontekst Playwright na całą sesję testową."""
    with sync_playwright() as p:
        yield p


@pytest.fixture()
def api(pw) -> APIRequestContext:
    """Kontekst HTTP Playwright ze stałą bazą URL."""
    ctx = pw.request.new_context(base_url=BASE_URL)
    yield ctx
    ctx.dispose()


def test_root_and_tasks_flow(api: APIRequestContext):
    # 1) GET /
    r = api.get("/")
    assert r.ok, f"/ -> {r.status} {r.text()}"
    data = r.json()
    assert any(v == "Witaj" for v in data.values())

    # 2) GET /tasks (lista)
    r = api.get("/tasks")
    assert r.ok
    tasks = r.json()
    assert isinstance(tasks, list)

    # 3) POST /tasks (utworzenie)
    r = api.post(
        "/tasks",
        data=json.dumps({"title": "E2E task"}),
        headers={"Content-Type": "application/json"},
    )
    assert r.status == 201, r.text()
    created = r.json()
    tid = created["id"]
    assert tid >= 1

    # 4) PATCH /tasks/{id} (done=True)
    r = api.patch(
        f"/tasks/{tid}",
        data=json.dumps({"done": True}),
        headers={"Content-Type": "application/json"},
    )
    assert r.ok, r.text()
    assert r.json()["done"] is True

    # 5) GET /tasks (zawiera nasze zadanie)
    r = api.get("/tasks")
    assert r.ok
    assert any(t["id"] == tid for t in r.json())

    # 6) DELETE /tasks/{id}
    r = api.delete(f"/tasks/{tid}")
    assert r.status == 204

    # 7) GET /tasks (już nie ma)
    r = api.get("/tasks")
    assert r.ok
    assert all(t["id"] != tid for t in r.json())
