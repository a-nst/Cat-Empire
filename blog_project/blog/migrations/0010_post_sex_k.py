# Generated by Django 3.2.9 on 2021-11-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sex_k',
            field=models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], default='Мужской', max_length=7),
        ),
    ]
