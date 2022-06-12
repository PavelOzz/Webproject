from django.db import models

class svyaz(models.Model):
    name = models.CharField('Имя',max_length=35)
    phone_number = models.CharField('Номер телефона', max_length=20)
    email = models.CharField('Email', max_length=50)
    message = models.CharField('Сообщение', max_length=300)

class menu(models.Model):
    name = models.CharField('Название',max_length=50)
    massa = models.CharField('Масса',max_length=15)
    price = models.CharField('Цена',max_length=15)
    picture = models.ImageField(upload_to='static/img/menupic')

    def __str__(self):
        return self.name