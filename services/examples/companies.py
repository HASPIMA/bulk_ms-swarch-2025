import time
from uuid import uuid4

from models.examples.company import Company


def generate_companies() -> list[Company]:
    generated: list[Company] = [
        Company(id=uuid4(), name=f'Company {i}')
        for i in range(1, 6)
    ]

    # Simulate a long-running task
    time.sleep(5)

    return generated
