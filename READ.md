# Flask TODO App ✅

Prosta aplikacja **TODO** napisana w Pythonie (Flask), z pseudobazą danych w pamięci.  
Projekt zawiera testy jednostkowe, raporty jakości i bezpieczeństwa oraz konfigurację Dockera/Podmana.

---

## 🚀 Uruchamianie lokalne

### 1. Klonowanie repozytorium
```bash
git clone <URL_Twojego_repo>
cd <nazwa_folderu>

2. Utworzenie i aktywacja wirtualnego środowiska
python -m venv .venv
. .venv\Scripts\Activate.ps1

3. Instalacja zależności
pip install -r requirements.txt

4. Uruchomienie aplikacji
$env:FLASK_APP="app"
python -m flask run
Aplikacja będzie dostępna pod adresem:
👉 http://127.0.0.1:5000/

🧪 Testy i Coverage
Uruchom wszystkie testy:

python -m pytest -q
Generowanie raportu coverage (JSON + w terminalu):


python -m pytest --cov=app --cov-branch --cov-report=term
python -m coverage json -o reports/coverage.json

Minimalne pokrycie wymagane: 80%

🔒 Raporty bezpieczeństwa
pip-audit (zależności Python)

python -m pip_audit -r requirements.txt --format json -o reports/pip-audit.json
Trivy (skan repozytorium – filesystem)

trivy fs --severity HIGH,CRITICAL --ignore-unfixed --exit-code 0 --format json --output reports/trivy-fs.json .
Trivy (skan obrazu)
Najpierw zbuduj obraz (Podman):


podman build -t flask-todo .
Następnie przeskanuj:


trivy image --severity HIGH,CRITICAL --ignore-unfixed --exit-code 0 --format json -o reports/trivy-image.json flask-todo
⚡ VS Code Tasks
W folderze .vscode/tasks.json znajdują się skonfigurowane taski, które generują wszystkie raporty jednym kliknięciem:

Reports: ALL (FS) → coverage + pip-audit + trivy-fs

Reports: ALL (IMAGE) → coverage + pip-audit + trivy-image

Uruchomienie:
Ctrl+Shift+P → odpala 3 raporty na raz

Ctrl+Shift+B → odpala Reports: ALL (FS) (domyślny task)

lub Ctrl+Shift+P → Tasks: Run Task → wybierz dowolny task

🐳 Docker / Podman
Budowa obrazu
podman build -t flask-todo .

Uruchomienie kontenera
podman run -p 5000:5000 flask-todo

Aplikacja dostępna pod adresem:
👉 http://127.0.0.1:5000/

📂 Struktura projektu
.
├── app/                # Kod aplikacji Flask
│   ├── __init__.py
│   ├── models.py
│   ├── repo.py
│   └── routes.py
├── tests/              # Testy jednostkowe (pytest)
│   ├── test_repo.py
│   └── test_routes.py
├── reports/            # Raporty JSON (coverage, pip-audit, trivy)
├── requirements.txt    # Zależności Python
├── Dockerfile          # Definicja obrazu
├── docker-compose.yml  # (opcjonalnie) do uruchamiania
└── README.md           # Dokumentacja
