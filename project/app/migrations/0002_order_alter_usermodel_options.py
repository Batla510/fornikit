# Generated by Django 5.0 on 2023-12-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='usermodel',
            options={'verbose_name': 'Человек', 'verbose_name_plural': 'Люди'},
        ),
    ]
