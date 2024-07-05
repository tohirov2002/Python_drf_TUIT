from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class ArticlesModel(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    annotation_uz = models.TextField()
    annotation_ru = models.TextField()
    description_uz = models.TextField()
    description_ru = models.TextField()
    keywords = models.CharField(max_length=255)
    references = models.CharField(
        max_length=255
    )  # Ustoz bunga kitob yoki havola yozilsa buldi dedi, Ushani uchun buni matinli maydon qilib oldim
    date_time = models.DateTimeField(auto_now_add=True)
    eye = models.IntegerField(default=0)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_uz

    class Meta:
        db_table = "article"
        verbose_name = "Article"
        verbose_name_plural = "Articles"
