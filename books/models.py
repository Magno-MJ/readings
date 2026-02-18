from django.db import models

from users.models import User

class Book(models.Model):
    name = models.CharField(max_length=100)
    quantity_of_pages = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'user'], name='unique_book_per_user')
        ]