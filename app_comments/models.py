from django.db import models
from django.contrib.auth import get_user_model

from app_articles.models import ArticlesModel


class Comments(models.Model):
    comment_text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment_reply_to = models.ForeignKey(
        "Comments", on_delete=models.CASCADE, null=True
    )
    comment_doc = models.ForeignKey(ArticlesModel, on_delete=models.CASCADE)
    comment_status = models.BooleanField(default=True)
    comment_likes = models.ManyToManyField(
        get_user_model(), related_name="comment_likes", blank=True
    )
    comment_dislikes = models.ManyToManyField(
        get_user_model(), related_name="comment_dislikes", blank=True
    )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text

    class Meta:
        ordering = ["-create_date"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        db_table = "comments"
