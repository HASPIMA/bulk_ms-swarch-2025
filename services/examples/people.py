import time
from uuid import uuid4

from models.examples.person import Person


def generate_people():
    generated: list[Person] = [
        Person(id=uuid4(), name=f'John Doe {i}')
        for i in range(1, 6)
    ]

    # Simulate a long-running task
    time.sleep(5)

    return generated
