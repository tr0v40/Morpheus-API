# Generated by Django 2.1.5 on 2019-01-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Materiais', '0001_initial'),
        ('Pacotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insercao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtde', models.IntegerField()),
                ('peso_unit', models.DecimalField(decimal_places=3, max_digits=10)),
                ('peso_liq', models.DecimalField(decimal_places=3, max_digits=10)),
                ('ins_material', models.ManyToManyField(to='Materiais.Materiais')),
                ('ins_pacote', models.ManyToManyField(to='Pacotes.Pacotes')),
            ],
        ),
    ]