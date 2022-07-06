from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Ticket(models.Model):
    ticket = models.CharField(max_length=150, null = True)
    date_added = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    def __str__(self):
        return self.ticket
    class Meta:
       ordering = ['-date_added',]

class FreeTipsGame(models.Model):
    STATUS_CHOICES = (
        ('Running', 'Running'),
        ('Won', 'Won'),
        ('Lost', 'Lost'),
    )

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null = True)

    country = models.CharField(max_length = 200, null = True)

    home_team = models.CharField(max_length = 200, null = True)

    away_team = models.CharField(max_length = 200, null = True)

    prediction = models.CharField(max_length = 100, null = True)

    odds = models.CharField(max_length = 100, null = True, blank = True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='running')

    class Meta:
        ordering = ['-ticket__date_added',]

    def __str__(self):
       return str(self.home_team)

class vipTipsGame(models.Model):
    STATUS_CHOICES = (
        ('Running', 'Running'),
        ('Won', 'Won'),
        ('Lost', 'Lost'),
    )

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null = True)

    country = models.CharField(max_length = 200, null = True)

    home_team = models.CharField(max_length = 200, null = True)

    away_team = models.CharField(max_length = 200, null = True)

    prediction = models.CharField(max_length = 100, null = True)

    odds = models.CharField(max_length = 100, null = True, blank = True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='running')

    class Meta:
        ordering = ['-ticket__date_added',]

    def __str__(self):
       return str(self.home_team)

class RollTipsGame(models.Model):
    STATUS_CHOICES = (
        ('Running', 'Running'),
        ('Won', 'Won'),
        ('Lost', 'Lost'),
    )

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null = True)

    country = models.CharField(max_length = 200, null = True)

    home_team = models.CharField(max_length = 200, null = True)

    away_team = models.CharField(max_length = 200, null = True)

    prediction = models.CharField(max_length = 100, null = True)

    odds = models.CharField(max_length = 100, null = True, blank = True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='running')

    class Meta:
        ordering = ['-ticket__date_added',]

    def __str__(self):
       return str(self.home_team)

class SingleBet(models.Model):
    STATUS_CHOICES = (
        ('Running', 'Running'),
        ('Won', 'Won'),
        ('Lost', 'Lost'),
    )

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null = True)

    country = models.CharField(max_length = 200, null = True)

    home_team = models.CharField(max_length = 200, null = True)

    away_team = models.CharField(max_length = 200, null = True)

    prediction = models.CharField(max_length = 100, null = True)

    odds = models.CharField(max_length = 100, null = True, blank = True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='running')

    class Meta:
        ordering = ['-ticket__date_added',]

    def __str__(self):
       return str(self.home_team)

class Profile(models.Model):
    STATUS_CHOICES = (
        ('free', 'free'),
        ('vip', 'vip'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=10, choices=STATUS_CHOICES, default='free')

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
