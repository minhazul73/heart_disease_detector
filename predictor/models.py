from django.db import models

class PatientInput(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    cholesterol_level = models.FloatField()
    blood_pressure = models.FloatField()
    diabetes = models.BooleanField()
    prediction_result = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
