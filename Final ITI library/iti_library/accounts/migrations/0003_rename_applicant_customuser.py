# Generated by Django 5.1.1 on 2024-09-17 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_customuser_applicant'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('books', '0002_remove_book_isbn'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Applicant',
            new_name='CustomUser',
        ),
    ]
