from django.db import models


class exam(models.Model):
    question = models.CharField('Вопрос', max_length=250)
    answers = models.TextField('Все возможные ответы на вопросы')
    true_answer = models.CharField('Правильный ответ на вопрос', max_length=50)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'