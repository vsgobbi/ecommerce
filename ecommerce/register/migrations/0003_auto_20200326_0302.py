# Generated by Django 3.0.4 on 2020-03-26 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20200326_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Não declarar')], default='M', max_length=1),
        ),
    ]
