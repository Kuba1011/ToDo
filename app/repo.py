from typing import Dict, List, Optional   # import typów pomocniczych
from .models import Task                  # import modelu Task

class Repo:                               # klasa Repo = pseudo-baza danych
    def __init__(self):
        self._store: Dict[int, Task] = {} # słownik id → Task, przechowuje zadania
        self._next_id: int = 1            # licznik id, zaczynamy od 1

    def add(self, task: Task) -> Task:    # dodanie nowego zadania
        if task.id == 0:                  # UWAGA: tutaj musi być '==' (porównanie), a nie '='
            task.id = self._next_id       # nadaj nowe id
        self._store[task.id] = task       # zapisz zadanie w słowniku
        self._next_id = max(self._next_id, task.id + 1)  # zwiększ licznik
        return task                       # zwróć zadanie

    def get(self, task_id: int) -> Optional[Task]:   # pobierz zadanie po id
        return self._store.get(task_id)              # zwraca Task lub None

    def list(self) -> List[Task]:                    # lista wszystkich zadań
        return list(self._store.values())

    def update(self, task: Task) -> Task:            # aktualizacja istniejącego zadania
        if task.id not in self._store:               # jeśli nie istnieje...
            raise KeyError("Task not found")         # ...błąd
        self._store[task.id] = task                  # nadpisz zadanie
        return task

    def delete(self, task_id: int) -> bool:          # usuń zadanie po id
        return self._store.pop(task_id, None) is not None  # True jeśli usunięto
