from users.dtos import CreateUserDto
from users.exceptions import UserAlreadyExistsException
from users.models import User

class CreateUserService():
    def execute(self, create_user_dto: CreateUserDto):
        user_email = create_user_dto.email
        
        user_already_exists = User.objects.filter(email=user_email).exists()

        if user_already_exists:
            raise UserAlreadyExistsException()
        
        user = User(
            first_name=create_user_dto.first_name,
            last_name=create_user_dto.last_name,
            email=create_user_dto.email,
        )

        user.set_password(create_user_dto.password)

        user.save()
