# Generated by Django 4.1.3 on 2022-11-11 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=30)),
                ('data_nascimento', models.DateField()),
            ],
        ),
    ]
