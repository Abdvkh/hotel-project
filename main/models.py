from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

WEEKDAYS = [
  (1, "Monday"),
  (2, "Tuesday"),
  (3, "Wednesday"),
  (4, "Thursday"),
  (5, "Friday"),
  (6, "Saturday"),
  (7, "Sunday"),
]


class Hotel(models.Model):
    """docstring for Hotel."""

    name = models.CharField("Hotel's name", max_length=50)
    stars = models.PositiveIntegerField(
                                        'Stars',
                                        validators=[
                                                    MinValueValidator(0),
                                                    MaxValueValidator(5)
                                                    ]
                                        )
    owner = models.CharField('Fullname of owner', max_length=100)


class OpeningHours(models.Model):
    """docstring"""

    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __unicode__(self):
        return u'%s: %s - %s' % (self.get_weekday_display(),
                                 self.from_hour, self.to_hour)


class Image(models.Model):
    """docstring for Images."""

    image = models.ImageField(upload_to='hotel')
