# Generated by Django 2.1.5 on 2019-01-25 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pacote', models.CharField(max_length=50)),
            ],
        ),
    ]
