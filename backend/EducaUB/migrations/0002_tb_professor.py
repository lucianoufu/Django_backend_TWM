# Generated by Django 3.1.4 on 2020-12-20 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EducaUB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EducaUB.tb_pessoa')),
            ],
        ),
    ]