from django.db import models

# Create your models here.

class ReserveTable(models.Model):
    name = models.CharField(max_length = 15, verbose_name = '予約者氏名')
    part = models.CharField(default = '',max_length=5, choices = (('Vo','Vo'), ('Gt','Gt'), ('Ba','Ba'), ('Fr','Dr'), ('Key', 'Key'), ('その他','その他')), verbose_name = '予約者のパート')
    band_or_individual = models.CharField(default = '',max_length = 5, choices = (('バンド練習', 'バンド練習'),('個人練習', '個人練習')), verbose_name = '個人練習orバンド練習')
    modified = models.DateTimeField(auto_now = True, verbose_name = '予約完了した時刻')
    def __str__(self):
        return self.name
class StudioTable(models.Model):
    reserve = models.OneToOneField(ReserveTable, on_delete=models.CASCADE, verbose_name = '予約情報', null = True, blank = True)

    period = models.CharField(default = '',verbose_name = '予約時限', max_length = 5, choices = (('1限','1限'),('2限','2限'),('昼休み','昼休み'),('3限','3限'),('4限','4限'),('5限','5限'),('6限','6限'),('7限','7限')))
    date = models.DateField(verbose_name = '予約日', null = True)
    
    def __str__(self):
        return f"{self.date}({self.period})"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["date", "period"],
                name="studio_unique"
            ),
        ]
