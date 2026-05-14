from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Book:
    id: UUID = field(default_factory=uuid4)
    name: str = ""
    quantity_of_pages: int = 0
    isbn: str = ""
