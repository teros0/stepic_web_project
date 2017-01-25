from __future__ import unicode_literals

from django.db import models, connection
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * from qa_question q ORDER BY q.added_at DESC""")
            result_list = cursor.fetchall()
        return result_list

    def popular(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * from qa_question q ORDER BY q.rating DESC""")
            result_list = cursor.fetchall()
        return result_list

class Question(models.Model):
        title = models.CharField(max_length=255)
        text = models.TextField()
        added_at = models.DateTimeField(auto_now_add=True)
        rating = models.IntegerField(default=0)
        author = models.ForeignKey(User, related_name="question_author")
        likes = models.ManyToManyField(User, related_name="question_likes", blank=True)

        objects = QuestionManager()

        class Meta:
        ordering = ('-added_at',)

        def __unicode__(self):
            return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ('added_at',)

    def __unicode__(self):
        return 'Answer by {}'.format(self.author)