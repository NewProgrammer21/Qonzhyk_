# Generated by Django 3.2.7 on 2022-05-21 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universystem', '0015_auto_20220521_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='srp',
            name='image',
        ),
    ]