from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) :
        return self.name

class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self) :
        return self.name
    
class University(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=50)
    logo = models.ImageField(null=True , blank=True)
    type = models.CharField(max_length=100)
    overview = models.TextField()
    stablished_year = models.IntegerField()
    student_amount = models.IntegerField()
    int_student_amount = models.IntegerField()
    address = models.CharField(max_length=500,default='empty')
    website = models.URLField()
    admission_rate = models.FloatField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()