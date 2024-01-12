from django.db import models
from django.contrib.auth.models import User


class Text(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField('Текст')

    def __str__(self):
        return self.text[:]

    class Meta:
        verbose_name = 'Глобальный текст'
        verbose_name_plural = 'Глобальный текст'


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    text = models.ForeignKey(
        Text, related_name='news', on_delete=models.CASCADE, null=False, verbose_name='Текст'
    )
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']


class Workers(models.Model):
    id = models.AutoField(primary_key=True)
    surname = models.CharField('Фамилия', max_length=20)
    name = models.CharField('Имя', max_length=20)
    patronymic = models.CharField('Отчество', max_length=20)
    text = models.ForeignKey(
        Text, related_name='workers', on_delete=models.CASCADE, null=False, verbose_name='Текст'
    )
    birthdate = models.DateField('Дата рождения')

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Aktirovka(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Название', max_length=50)
    text = models.ForeignKey(
        Text, related_name='aktirovka', on_delete=models.CASCADE, null=False, verbose_name='Текст'
    )
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Актировка'
        verbose_name_plural = 'Актировки'
        ordering = ['-date']


class Appeal(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Название', max_length=50)
    text = models.ForeignKey(
        Text, related_name='appeal', on_delete=models.CASCADE, null=False, verbose_name='Текст'
    )
    user = models.ForeignKey(
        User, related_name='user', on_delete=models.CASCADE, null=False, verbose_name='Индефикатор пользователя'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обращения граждан'
        verbose_name_plural = 'Обращения граждан'
