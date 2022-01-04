# Generated by Django 4.0 on 2022-01-04 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_alter_log_options_med_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='med',
        ),
        migrations.AddField(
            model_name='med',
            name='log',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.log'),
            preserve_default=False,
        ),
    ]