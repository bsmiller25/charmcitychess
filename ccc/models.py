from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uscf_id = models.IntegerField(null=True, blank=True)
    chesscom_id = models.CharField(max_length=100, null=True, blank=True)
    lichess_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return('{}, {}'.format(self.user.first_name, self.user.last_name))
    
@receiver(post_save, sender=User)
def create_user_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_member(sender, instance, **kwargs):
    instance.member.save()
