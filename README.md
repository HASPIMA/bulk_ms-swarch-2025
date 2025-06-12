# MeetUN Bulk Processing API

- [MeetUN Bulk Processing API](#meetun-bulk-processing-api)
  - [Environment Variables](#environment-variables)
  - [Running and setting up the project](#running-and-setting-up-the-project)
    - [Docker](#docker)
      - [Regenerate the ignore file](#regenerate-the-ignore-file)
      - [Running everything](#running-everything)
      - [Running only the Processing API](#running-only-the-processing-api)
        - [Build the Docker image](#build-the-docker-image)
        - [Running the image](#running-the-image)
    - [Local development](#local-development)
      - [Setup locally](#setup-locally)
      - [Run Locally](#run-locally)
        - [Running the Bulk microservice](#running-the-bulk-microservice)
        - [Running the Worker](#running-the-worker)
        - [Running Flower](#running-flower)
        - [Running Redis](#running-redis)

## Environment Variables

To run this project, you will need to add the following environment
variables to your .env file, you can check
[this example](.env.example) file too

- `PORT` - The port where the server will run on
- `CELERY_BROKER_URL` - The URL of the Celery broker (e.g., Redis
or RabbitMQ)
- `CELERY_RESULT_BACKEND` - The URL of the Celery result backend (e.g., Redis or
RabbitMQ)

## Running and setting up the project

### Docker

#### Regenerate the ignore file

You may want to regenerate the `.dockerignore` file if you modified either
`.gitignore` or `.gcloudignore` files. You can do this by running the following
commands:

> [!NOTE]
> This command will overwrite the `.dockerignore` file with all the
> contents of the `.gitignore` and `.gcloudignore` files.

```sh
cat .gitignore .gcloudignore > .dockerignore
```

#### Running everything

To run the project with Docker, you can use the following command:

```sh
docker-compose up --build
```

This will build the Docker image and run the Processing API, Worker,
Flower, and Redis containers. The Processing API will be available
at `http://localhost:8080` (or the port you specified in the
[`.env` file](#environment-variables)). The Worker and Flower will be
available at `http://localhost:5555` (or the port you specified in
the [`.env` file](#environment-variables)). You can stop the
containers by pressing `Ctrl+C` or by running:

```sh
docker-compose down
```

> [!NOTE]
> If you want to run the project in detached mode, you can use the `-d` flag:

```sh
docker-compose up --build -d
```

> [!TIP]
> If you want to destroy the containers and remove the volumes, you can use the `--volumes` flag:

```sh
docker-compose down --volumes
```

> [!TIP]
> If you want to remove the images, you can use the `--rmi` flag:

```sh
docker-compose down --rmi all
```

#### Running only the Processing API

##### Build the Docker image

```sh
docker build -t mu-bulk-ms:$(git rev-parse HEAD) . # Tag it with the current commit hash
docker build -t mu-bulk-ms:latest . # Tag it as latest
```

##### Running the image

You could setup a port by setting an environment variable
`PORT` to the desired port number. By default it is set to
`8080`. In case you want to change the port number, you can
do so by running the following command, which will set the
port number to `8001` and then map the port `8000` of the
host machine to the port `8001` of the container.

```bash
docker run -e PORT=8001 -p 8000:8001 mu-bulk-ms
```

### Local development

#### Setup locally

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

2. Install required packages

    ```sh
    uv sync
    ```

3. Activate the
[environment](https://docs.astral.sh/uv/pip/environments/):

    ```sh
    uv venv
    ```

#### Run Locally

There are some components to run:

1. [**Bulk microservice**](#running-the-bulk-microservice) - The web
server that will handle the requests
2. [**Worker**](#running-the-worker) - The worker that will process
the requests using the
[competing consumer pattern](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CompetingConsumers.html)
3. [**Flower**](#running-flower) (optional) - The web UI for
monitoring the Celery tasks
4. [**Redis**](#running-redis) (required if environment variable not
provided) - The message broker (for now) and result backend for Celery

##### Running the Bulk microservice

Once [setup](#setup-locally), you should be able to run the project
by running:

```sh
fastapi dev main.py
```

If you don't want file changes to re-run the project you should run instead:

```sh
fastapi dev main.py
```

Alternatively, you can run the [main](main.py) script directly with:

```sh
uv run main.py
```

##### Running the Worker

The worker is responsible for processing the requests. You can run it with:

```sh
celery -A worker.celery worker --loglevel=info
```

##### Running Flower

Flower is a web UI for monitoring the Celery tasks. You can run it with:

```sh
celery --broker=<CELERY_BROKER_URL> flower --port=5555
```

You can then access it at `http://localhost:5555` (or the port you specified).

##### Running Redis

> [!WARNING]
> The way this command is setup is for redis to be ephemeral. If you
> wish to preserve the volume, remove the `--rm` flag.

If you don't have Redis installed, you can run it with Docker. Like
this:

```sh
docker run -it --rm -p 6379:6379 redis:7-alpine
```

You can then access it at `redis://localhost:6379/0` (or the port you specified).
