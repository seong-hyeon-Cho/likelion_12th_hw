# Generated by Django 5.0.3 on 2024-05-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post_stitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='stitle',
            field=models.CharField(max_length=10),
        ),
    ]