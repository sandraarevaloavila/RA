# Generated by Django 4.1 on 2022-09-07 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0004_contactenos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactenos',
            name='mensaje',
            field=models.TextField(),
        ),
    ]
