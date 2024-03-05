from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email= models.EmailField(max_length=20)
    age = models.IntegerField()
    contact= models.CharField(max_length=15)
    date_of_birth= models.DateField()
    class Meta:
        db_table = 'student'

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
          return self.first_name
class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email= models.CharField(max_length=20)
    def __str__(self):
        return self.first_name
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=20)
    auther = models.CharField(max_length=20)
    date_created =models.IntegerField()

