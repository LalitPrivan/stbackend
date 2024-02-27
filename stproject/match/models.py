from django.db import models


class TeamA(models.Model):
    time = models.BigIntegerField(primary_key=True)
    shot = models.CharField(max_length=50,)
    made = models.CharField(max_length=50, null=True, blank=True)
    made_SJN = models.CharField(max_length=50, null=True, blank=True)
    made_locx = models.FloatField(null=True, blank=True)
    made_locy = models.FloatField(null=True, blank=True)
    made_assist = models.CharField(max_length=50, null=True, blank=True)
    made_shottype = models.CharField(max_length=50, null=True, blank=True)
    miss = models.CharField(max_length=50, null=True, blank=True)
    miss_outb = models.CharField(max_length=50, null=True, blank=True)
    miss_reb = models.CharField(max_length=50, null=True, blank=True)
    o_reb_SJN = models.CharField(max_length=50, null=True, blank=True)
    d_reb_DJN = models.CharField(max_length=50, null=True, blank=True)
    quater = models.CharField(max_length=50, null=True, blank=True)
    

    def _str_(self):
        return f"{self.id} - {self.time} - {self.shot} - {self.made}"