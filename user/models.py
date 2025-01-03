from django.urls import reverse
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10, unique=True, db_column='username')
    password = models.CharField(max_length=20, db_column='user_password')
    Email = models.EmailField(unique=True, db_column='user_email')
    phone = models.CharField(max_length=20, unique=True, db_column='user_phone')

    def __str__(self):
        return f'{self.id}_{self.username}'

    def get_absolute_url(self):
        return reverse('load_user', args=[self.id])

    class Meta:
        db_table = 'users'