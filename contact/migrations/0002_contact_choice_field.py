# Generated by Django 4.0.4 on 2022-04-26 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='choice_field',
            field=models.CharField(choices=[('1', 'First'), ('2', 'Second')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]