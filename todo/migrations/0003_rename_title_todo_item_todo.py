# Generated by Django 5.0.4 on 2024-04-16 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_item_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo_item',
            old_name='title',
            new_name='todo',
        ),
    ]