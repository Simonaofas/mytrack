# Generated by Django 5.0.2 on 2024-04-16 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytrack', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='EmergencyAlert',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]