# Lekki obraz bazowy Pythona
FROM python:3.13-slim

# Nie zapisuj .pyc i buforuj stdout/stderr (lepsze logi)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app

# Praca w /app
WORKDIR /app

# Najpierw zależności (lepsze cache warstw)
COPY requirements.txt /app/
RUN python -m pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Potem kod aplikacji
COPY app /app/app

# Flask dev server nasłuchuje na 5000
EXPOSE 5000

# Start aplikacji
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
