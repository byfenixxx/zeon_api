# Generated by Django 4.0.3 on 2022-04-01 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_collection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'Цвет', 'verbose_name_plural': 'Цвета'},
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.product', verbose_name='Изображения')),
            ],
        ),
    ]
