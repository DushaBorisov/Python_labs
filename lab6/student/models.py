from django.db import models


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    university = models.CharField(max_length=20)
    course_number = models.IntegerField()

    class Meta:
        db_table = 'students'
