# Generated by Django 3.2.20 on 2023-08-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='product',
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.CharField(default='Ask your question here', max_length=254),
        ),
    ]
