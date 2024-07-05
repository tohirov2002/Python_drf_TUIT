from django.db import models


class Requirements(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    annotation_uz = models.CharField(max_length=255)
    annotation_ru = models.CharField(max_length=255)
    description_uz = models.TextField()
    description_ru = models.TextField()
    problem_uz = models.CharField(max_length=255)
    problem_ru = models.CharField(max_length=255)
    solution_uz = models.CharField(max_length=255)
    solution_ru = models.CharField(max_length=255)
    learned_uz = models.CharField(max_length=255)
    learned_ru = models.CharField(max_length=255)
    analysis_uz = models.CharField(max_length=255)
    analysis_ru = models.CharField(max_length=255)

    def __str__(self):
        return self.title_uz

    class Meta:
        db_table = "requirements"
        verbose_name = "Requirement"
        verbose_name_plural = "Requirements"
