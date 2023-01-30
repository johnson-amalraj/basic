from django.db import model

# Create a Model here
class Todo (models.Model):
    added_date = models.DateTimeField()
    text       = models.CharField(max_length=200)
