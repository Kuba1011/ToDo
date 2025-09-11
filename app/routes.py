from flask import Blueprint, jsonify, request, abort      # importuje narzędzia Flask do tworzenia endpointów i odpowiedzi HTTP
from .repo import Repo                                    # importuje nasze repozytorium (pseudo-baza w pamięci)
from .models import Task                                  # importuje model Task (id, title, done)

bp = Blueprint("api", __name__)                           # tworzy blueprint (grupę tras) o nazwie "api"
repo = Repo()                                             # tworzy jedną instancję repo (przechowuje zadania w słowniku)

@bp.get("/tasks")                                         # obsługuje metodę GET na ścieżce /tasks
def list_tasks():
    return jsonify([t.__dict__ for t in repo.list()]), 200  # zamienia obiekty Task na dict i zwraca listę zadań (HTTP 200)

@bp.post("/tasks")                                        # obsługuje metodę POST na /tasks (tworzenie nowego zadania)
def create_task():
    payload = request.get_json(silent=True) or {}         # pobiera JSON z requestu jako dict (albo pusty dict)
    title = (payload.get("title") or "").strip()          # wyciąga pole "title" i przycina spacje
    if not title:                                         # jeśli tytuł jest pusty po przycięciu...
        abort(400, "Tytuł zadania jest wymagany")         # ...zwraca błąd 400 (Bad Request) z komunikatem
    task = Task(id=0, title=title, done=False)            # tworzy nowe zadanie (id=0 oznacza: nada je repo)
    repo.add(task)                                        # dodaje zadanie do repo (repo nada ID)
    return jsonify(task.__dict__), 201                    # zwraca utworzone zadanie (HTTP 201 Created)

@bp.patch("/tasks/<int:task_id>")                         # obsługuje PATCH /tasks/<id> (częściowa aktualizacja)
def update_task(task_id: int):
    payload = request.get_json(silent=True) or {}         # pobiera JSON z danymi do zmiany
    task = repo.get(task_id)                              # próbuje znaleźć zadanie o podanym id
    if not task:                                          # jeśli nie istnieje...
        abort(404, "Zadanie nie istnieje")                # ...404 Not Found

    if "title" in payload:                                # jeśli w payloadzie jest pole "title"...
        new_title = (payload["title"] or "").strip()      # ...odczytuje je i przycina spacje
        if not new_title:                                 # jeśli po przycięciu jest puste...
            abort(400, "Tytuł nie może być pusty")        # ...błąd 400
        task.title = new_title                            # ustawia nowy tytuł

    if "done" in payload:                                 # jeśli w payloadzie jest pole "done"...
        task.done = bool(payload["done"])                 # ...ustawia wartość logiczną True/False

    repo.update(task)                                     # zapisuje zmiany w repo
    return jsonify(task.__dict__), 200                    # zwraca zaktualizowane zadanie (HTTP 200)

@bp.delete("/tasks/<int:task_id>")                        # obsługuje DELETE /tasks/<id>
def delete_task(task_id: int):
    ok = repo.delete(task_id)                             # próbuje usunąć zadanie; True jeśli istniało i usunięto
    if not ok:                                            # jeśli nie istniało...
        abort(404, "Zadanie nie istnieje")                # ...404 Not Found
    return "", 204                                        # brak treści i kod 204 No Content
