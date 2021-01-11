from django.db import models

# Create your models here.
class PageHit(models.Model):
    pagehit_id = models.AutoField(primary_key=True)
    pagehit_session_id = models.CharField(max_length=100, blank=True, null=True)
    pagehit_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagehit'
