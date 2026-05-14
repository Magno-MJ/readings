from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Book:

    name: str
    quantity_of_pages: int
    isbn: str

    id: UUID = field(default_factory=uuid4)
