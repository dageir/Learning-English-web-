from django.db import models

#Первый вариант модели тестирования (старый вариант)
class Exam(models.Model):
    question = models.CharField('Вопрос', max_length=250)
    answers = models.TextField('Все возможные ответы на вопросы')
    true_answer = models.CharField('Правильный ответ на вопрос', max_length=50)

    def __str__(self):
        return self.question

    def answer(self):
        key_ans = '33ijf9asjds9aj'
        answer = str(self.answers).split(key_ans)
        return answer

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

#Модель тестирования (второй вариант, с ограниченным кол-вом ответов)
class TestingWithChangeAnswer(models.Model):

    question = models.TextField('Вопрос')
    answer1 = models.CharField('Первый вариант ответа', max_length=250)
    answer2 = models.CharField('Второй вариант ответа', max_length=250)
    answer3 = models.CharField('Третий вариант ответа', max_length=250)
    answer4 = models.CharField('Четвёртый вариант ответа', max_length=250)
    true_answer = models.CharField('Правильный ответ на вопрос', max_length=250)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Тестирование'
        verbose_name_plural = 'Тестирования'

