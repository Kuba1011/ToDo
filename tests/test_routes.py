from app import app as flask_app                        # obiekt Flask

def test_root_hello_world():
    client = flask_app.test_client()                    # klient testowy
    r = client.get("/")                                 # GET /
    assert r.status_code == 200
    data = r.get_json()                                 #  pobierz JSON, nie r.get()
    # W zależności od Twojej wersji klucz może być "Wiadomość" (PL) albo "message" (EN)
    assert ("Wiadomość" in data) or ("message" in data)

def test_tasks_crud_flow():
    c = flask_app.test_client()

    r = c.get("/tasks")
    assert r.status_code == 200
    assert r.get_json() == []

    r = c.post("/tasks", json={"title": "Kup mleko"})
    assert r.status_code == 201
    t = r.get_json()
    assert t["id"] == 1
    assert t["title"] == "Kup mleko"
    assert t["done"] is False

    r = c.patch("/tasks/1", json={"done": True})
    assert r.status_code == 200
    assert r.get_json()["done"] is True

    r = c.patch("/tasks/1", json={"title": "Kup mleko i chleb"})
    assert r.status_code == 200
    assert r.get_json()["title"] == "Kup mleko i chleb"

    r = c.delete("/tasks/1")
    assert r.status_code == 204

    r = c.get("/tasks")
    assert r.status_code == 200
    assert r.get_json() == []

def test_post_requires_title():
    c = flask_app.test_client()
    r = c.post("/tasks", json={})  # brak "title"
    assert r.status_code == 400

def test_patch_not_found():
    c = flask_app.test_client()
    r = c.patch("/tasks/999", json={"done": True})
    assert r.status_code == 404

def test_patch_title_cannot_be_empty():
    """PATCH z pustym tytułem → 400"""
    c = flask_app.test_client()
    create_resp = c.post("/tasks", json={"title": "X"})
    assert create_resp.status_code == 201
    task_id = create_resp.get_json()["id"]

    r = c.patch(f"/tasks/{task_id}", json={"title": "   "})
    assert r.status_code == 400

def test_delete_not_found():
    c = flask_app.test_client()
    r = c.delete("/tasks/999")
    assert r.status_code == 404
