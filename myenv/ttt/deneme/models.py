from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class School(models.Model):
    city = models.ForeignKey(City, null=True, on_delete= models.CASCADE)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class User(models.Model):
    TYPE = (
        ('Müdür', 'Müdür'),
        ('Öğretmen', 'Öğretmen'),
        ('Öğrenci', 'Öğrenci')
    )
    type = models.CharField(max_length=100, null=True, choices=TYPE)
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    city = models.ForeignKey(City, null=True, on_delete= models.CASCADE)
    school = models.ForeignKey(School, null=True, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

