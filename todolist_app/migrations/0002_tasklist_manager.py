# Generated by Django 4.0 on 2021-12-29 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('todolist_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='manager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
