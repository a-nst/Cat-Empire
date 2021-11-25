from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    M='Мужской'
    G= 'Женский'

    sex=[
        (M,'Мужской'), 
        (G,'Женский')
        ]

    title = models.CharField(max_length=200, verbose_name='Имя котика')
    img = models.ImageField(upload_to = 'media/images/', null=True, blank=True,verbose_name='Фотография котика')
    sex_k =models.CharField(
        verbose_name='Пол котика',
        max_length = 7,
        choices = sex,
        default = 'Мужской'
    )
    body = models.TextField(verbose_name='Описание котика')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])