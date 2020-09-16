# Generated by Django 3.1.1 on 2020-09-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('sobrenome', models.CharField(max_length=150)),
                ('bairro', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'voluntarios',
            },
        ),
    ]
