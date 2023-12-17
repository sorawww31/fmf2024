from django.db import models

# Create your models here.

class StudioTable(models.Model):
    name = models.CharField(max_length = 15, verbose_name = '予約者氏名')
    band_or_individual = models.CharField(choices = ((1, 'バンド練習'),(2, '個人練習')))
    date = models.DateField(verbose_name = '日付')
    #grade = models.CharField(choices =((1,'1年生'),(2, '2年生'),(2,'2年生'),(3,'3年生'),(4,'その他')), verbose_name = '学年')
    period = models.CharField(choices = ((1,'1限'),(2,'2限'),(3,'昼休み'),(4,'3限'),(5,'4限'),(6,'5限'),(7,'6限'),(8,'7限')))
