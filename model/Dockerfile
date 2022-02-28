FROM python:3.8.12-slim-buster
ARG YOUR_ENV
ENV BENTO_HOME=/bento \
    POETRY_VERSION=1.1.12 \
	YOUR_ENV=${YOUR_ENV}
WORKDIR ${BENTO_HOME}
RUN pip install "poetry==$POETRY_VERSION"
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi
COPY ./bentoml /root/bentoml
COPY . .
EXPOSE 5000
CMD bentoml serve ./summarize/service.py:svc --reload
