# Generated by Django 2.1.5 on 2019-01-25 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porto', models.CharField(max_length=50)),
                ('cidade', models.CharField(blank=True, max_length=150, null=True)),
                ('pais', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
