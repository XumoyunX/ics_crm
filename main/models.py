from django.db import models
from clinet.models import User



class Course(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to="images/")
    text = models.TextField()
    price = models.IntegerField()


class Groups(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Students(models.Model):
    groups = models.ForeignKey(Groups, null=True, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    date = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.TextField()
    text = models.TextField()
    img = models.ImageField(upload_to="images/")
    date = models.DateTimeField(auto_now_add=True)


class Year(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Davomat(models.Model):
    students = models.ForeignKey(Students, null=True, on_delete=models.CASCADE)
    yaer = models.ForeignKey(Year, null=True, on_delete=models.CASCADE)
    kun = models.CharField(max_length=250)


class Moliya(models.Model):
    Qariz = 1
    Tuliq = 2
    students = models.ForeignKey(Students, null=True, on_delete=models.CASCADE)
    yaer = models.ForeignKey(Year, null=True, on_delete=models.CASCADE)
    price = models.IntegerField()
    tuliv = models.SmallIntegerField(choices=(
        (Qariz, "Qariz"),
        (Tuliq, "Tuliq")
    ))



class Fanta(models.Model):
    Qariz = 1
    Tuliq = 2
    groups = models.ForeignKey(Groups, null=True, on_delete=models.CASCADE)
    students = models.ForeignKey(Students, null=True, on_delete=models.CASCADE)
    yaer = models.ForeignKey(Year, null=True, on_delete=models.CASCADE)
    price = models.IntegerField()
    name = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    tuliv = models.SmallIntegerField(choices=(
        (Qariz, "Qariz"),
        (Tuliq, "Tuliq")
    ))




















