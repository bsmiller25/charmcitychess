from django.db import models



class Member(models.Model):
    first_name = models.CharField(max_length=100,
                                  null=True,
                                  blank=True)
    last_name = models.CharField(max_length=100,
                                 null=True,
                                 blank=True)
    uscf_id = models.BigIntegerField(null=True,
                                     blank=True)
    chesscom_userid = models.CharField(max_length=100,
                                       null=True,
                                       blank=True)
    lichess_userid = models.CharField(max_length=100,
                                      null=True,
                                      blank=True)
