# Generated by Django 4.0.3 on 2022-04-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_aboutus_rename_image_productimage_alter_help_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
    ]