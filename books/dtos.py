from dataclasses import dataclass

from users.models import User

@dataclass
class CreateBookDto:
    name: str
    quantity_of_pages: int
    user: User
