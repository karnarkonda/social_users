from django.db import models

# Create your models here.
class SocialMediaUser(models.Model):
    user_code = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=False)
    last_name = models.CharField(max_length=30, null=True, blank=False)
    friends = models.ManyToManyField("SocialMediaUser", related_name="to_friends")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["id"]
        verbose_name = "Social Media User"
        verbose_name_plural = "Social Media Users"
