# Generated by Django 4.0.4 on 2022-05-13 06:40

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('works_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('data', jsonfield.fields.JSONField(null=True)),
            ],
        ),
    ]