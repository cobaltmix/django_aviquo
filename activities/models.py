# Import the required default options
from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Extracurricular(models.Model):
    YEAR_CHOICES = [
        ("9th", "9th grade"),
        ("10th", "10th grade"),
        ("11th", "11th grade"),
        ("12th", "12th grade"),
    ]

    COST_CHOICES = [("Free", "Free"), ("Paid", "Paid")]

    EFFORT_CHOICES = [
        ("Low", "Low effort"),
        ("Medium", "Medium effort"),
        ("High", "High effort"),
        ("Hypercompetitive", "Hypercompetitive"),
    ]

    TYPE_CHOICES = [
        ("Summer Program", "Summer Program"),
        ("Competition", "Competition"),
        ("Scholarship", "Scholarship"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.ImageField(upload_to="images/")
    url = models.URLField()
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, blank=True, null=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, blank=True, null=True
    )
    cost = models.CharField(max_length=4, choices=COST_CHOICES, blank=True, null=True)
    effort = models.CharField(
        max_length=16, choices=EFFORT_CHOICES, blank=True, null=True
    )
    type = models.CharField(
        max_length=15, choices=TYPE_CHOICES, default="Summer Program"
    )

    def __str__(self):
        return self.name
