# Generated by Django 2.1.5 on 2019-01-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComInv', '0004_auto_20190127_1346'),
        ('Insercoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commercialinvoice',
            name='ci_insercao',
            field=models.ManyToManyField(to='Insercoes.Insercao'),
        ),
    ]
