# Generated by Django 3.1.4 on 2020-12-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EducaUB', '0002_tb_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_escola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_escola', models.TextField(max_length=255)),
                ('cep', models.IntegerField()),
                ('coordenada', models.TextField(max_length=20)),
            ],
        ),
    ]
