# Generated by Django 4.2 on 2024-10-25 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyiha', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]
