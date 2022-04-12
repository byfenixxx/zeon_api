# Generated by Django 4.0.3 on 2022-04-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_callbackrequest_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider_image/')),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Слайдеры',
            },
        ),
        migrations.AlterField(
            model_name='callbackrequest',
            name='did_callback',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=255),
        ),
    ]
