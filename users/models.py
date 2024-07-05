from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USERNAME_FIELD = "username"
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateTimeField(null=True, blank=True)  # birthday maydoni qo'shildi
    email = models.EmailField(unique=True, max_length=100)
    organization = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    scientific_degree = models.CharField(max_length=255)
    another_information = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="image/")

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        get_latest_by = "date_joined"
        ordering = ["date_joined"]


# Create your models here.
class PasswordResets(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "password_resets"
        unique_together = (("user", "created_at"),)
        index_together = (("user", "created_at"),)
        verbose_name = "Password Reset"
        verbose_name_plural = "Password Resets"
