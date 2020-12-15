from django.db import models

class Topic(models.Model):

    class Meta:
        db_table = "topic"

    dt          = models.DateTimeField(verbose_name="投稿日")
    comment     = models.CharField(verbose_name="コメント",max_length=2000)
    age         = models.IntegerField(verbose_name="年齢")


    def __str__(self):
        return self.comment
