FROM python:3.13
WORKDIR /app
COPY requirements.txt /app/    
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY app /app/app   
ENV FLASK_APP=app     
EXPOSE 5000      
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]