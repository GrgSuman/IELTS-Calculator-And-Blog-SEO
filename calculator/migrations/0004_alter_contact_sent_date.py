# Generated by Django 4.0.5 on 2022-07-03 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_contact_sent_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='sent_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]