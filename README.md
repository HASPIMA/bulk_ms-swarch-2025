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

