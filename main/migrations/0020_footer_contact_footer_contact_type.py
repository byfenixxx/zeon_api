# Generated by Django 4.0.3 on 2022-04-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='contact',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='contact_type',
            field=models.CharField(choices=[('PN', 'Phone Number'), ('EM', 'Email'), ('IG', 'Instagram'), ('TG', 'Telegram'), ('WA', 'Whatsapp')], max_length=2, null=True),
        ),
    ]