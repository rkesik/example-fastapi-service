from python:3.9.1

WORKDIR /app
RUN cd /app
COPY Pipfile.lock .
COPY Pipfile .
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
EXPOSE 8001
ENV PYTHONPATH "${PYTHONPATH}:/app/"
COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0",  "--port", "8000", "--log-level", "debug"]
