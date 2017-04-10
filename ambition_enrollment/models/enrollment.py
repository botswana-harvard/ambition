from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import GENDER, YES_NO


class Enrollment(BaseUuidModel):

    report_datetime = models.DateField()

    first_name = models.CharField(
        max_length=50)

    initials = models.CharField(
        max_length=3)

    gender = models.CharField(
        choices=GENDER,
        max_length=6)

    is_literate = models.CharField(
        choices=YES_NO,
        max_length=3)

    age = models.IntegerField(
        validators=MinValueValidator(16), MaxValueValidator(65))

    history = HistoricalRecords()

    class Meta:
        app_label = 'ambition_enrollment'
