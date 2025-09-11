from app.repo import Repo                 # import Repo (pseudo-baza)
from app.models import Task               # import modelu Task

def test_repo_add_get_update_delete():
    repo = Repo()                         # nowe repo w pamięci
    t = Task(id=0, title="A")             # nowe zadanie
    t = repo.add(t)                       # dodaj i nadaj id
    assert t.id == 1                      # pierwsze id = 1
    assert repo.get(1).title == "A"       # ✅ sprawdzamy tytuł, nie cały obiekt
    t.done = True                         # zmień status
    repo.update(t)                        # zapisz
    assert repo.get(1).done is True       # status zapisany
    assert repo.delete(1) is True         # usuń
    assert repo.get(1) is None            # już nie istnieje
