from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
        # 데이터베이스에 등록되지 않게 하기 위함
