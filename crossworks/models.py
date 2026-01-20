from django.db import models

class formapp(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254, unique=True)
    ph_no=models.IntegerField()
    submitted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name