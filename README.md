# MeetUN Bulk Processing API

## Environment Variables

To run this project, you will need to add the following environment
variables to your .env file, you can check
[this example](.env.example) file too

* `PORT` - The port where the server will run on
* `CELERY_BROKER_URL` - The URL of the Celery broker (e.g., Redis
or RabbitMQ)
* `CELERY_RESULT_BACKEND` - The URL of the Celery result backend (e.g., Redis or
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
