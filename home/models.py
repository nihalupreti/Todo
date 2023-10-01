from django.db import models
import uuid


class Data(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    email = models.EmailField(default="tom@gmail.com")
    todos = models.JSONField()

    # def __str__(self):
    #     tasks = self.todos["unfinished"]
    #     to_str = ""
    #     for task in tasks:
    #         to_str = f"{to_str} + {task}"
    #     return to_str
