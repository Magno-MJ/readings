from django.db import models
import uuid


class DjangoBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    quantity_of_pages = models.IntegerField()
    isbn = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "book"
