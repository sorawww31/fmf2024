from django.db import models

# Create your models here.

class StudioTable(models.Model):
    name = models.CharField(max_length = 15, verbose_name = '予約者氏名')
    part = models.CharField(max_length=5, choices = (('vo','Vo'), ('gt','Gt'), ('ba','Ba'), ('dr','Dr'), ('key', 'Key'), ('other','その他')), verbose_name = '予約者のパート')
    band_or_individual = models.CharField(max_length = 5, choices = (('Band', 'バンド練習'),('indi', '個人練習')), verbose_name = '個人練習orバンド練習')
    date = models.DateField(verbose_name = '予約日')
    modified = models.DateTimeField(auto_now = True, verbose_name = '予約完了した時刻')
    #grade = models.CharField(choices =((1,'1年生'),(2, '2年生'),(2,'2年生'),(3,'3年生'),(4,'その他')), verbose_name = '学年')
    period = models.CharField(verbose_name = '予約時限', max_length = 5, choices = (('1p','1限'),('2p','2限'),('break','昼休み'),('3p','3限'),('4p','4限'),('5p','5限'),('6p','6限'),('7p','7限')))

    def __str__(self):
        return self.name