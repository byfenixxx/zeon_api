# Generated by Django 4.0.3 on 2022-04-11 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_ourcontacts_alter_publicoffer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourcontacts',
            name='telegram',
            field=models.CharField(max_length=255, verbose_name='Номер в телеграм'),
        ),
        migrations.AlterField(
            model_name='ourcontacts',
            name='whatsapp',
            field=models.CharField(max_length=255),
        ),
    ]