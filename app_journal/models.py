from django.db import models


class JournalModel(models.Model):
    description_uz = models.TextField()
    description_ru = models.TextField()
    logo = models.ImageField(upload_to="images/")
    document_uz = models.FileField(upload_to="docs/")
    document_ru = models.FileField(upload_to="docs/")

    def __str__(self):
        return self.description_uz

    class Meta:
        db_table = "journal"
        verbose_name = "Journal"
        verbose_name_plural = "Journals"
