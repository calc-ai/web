FROM python:3.9.10-slim-buster
EXPOSE 8080
ARG YOUR_ENV
ENV APP_HOME=/app \
    POETRY_VERSION=1.1.12 \
    YOUR_ENV=${YOUR_ENV} \
    POETRY_VIRTUALENVS_CREATE=false
WORKDIR ${APP_HOME}
RUN pip install "poetry==$POETRY_VERSION"
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-ansi
COPY . . 
CMD streamlit run --server.port 8080 app.py
