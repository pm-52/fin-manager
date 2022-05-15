FROM python:3.10-bullseye

ENV POETRY_VERSION=1.1.13
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

RUN apt update && \
    apt upgrade -y

# install poetry 
RUN pip install "poetry==$POETRY_VERSION"

COPY [ \
    "pyproject.toml", \
    "poetry.lock", \
    "/app/" \
]

RUN mkdir -p ~/.config/pypoetry && \
    # Do not create virtual environment by poetry
    echo "[virtualenvs]\ncreate = false" >> ~/.config/pypoetry/config.toml && \
    cd /app && \
    poetry install --no-dev --no-root -n 
    # UWSGI is installed by pip, because system packages: uwsgi, uwsgi-core, etc.
    # are bound to system python, which is 3.9.2 for debian bullseye.
    # And for project is used python 3.8.12
    # pip install uwsgi

COPY . .

ENV PYTHONPATH /app

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
