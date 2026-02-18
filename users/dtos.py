from dataclasses import dataclass

@dataclass
class CreateUserDto:
    first_name: str
    last_name: str
    email: str
    password: str
