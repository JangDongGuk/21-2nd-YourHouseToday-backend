# Generated by Django 3.2.4 on 2021-06-23 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_kakao_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='kakao_id',
            field=models.CharField(max_length=20),
        ),
    ]