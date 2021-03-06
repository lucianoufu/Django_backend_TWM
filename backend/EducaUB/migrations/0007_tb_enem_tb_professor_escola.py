# Generated by Django 3.1.4 on 2020-12-20 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EducaUB', '0006_tb_disciplina_estudante'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_professor_escola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EducaUB.tb_escola')),
                ('id_professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EducaUB.tb_professor')),
            ],
        ),
        migrations.CreateModel(
            name='tb_enem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FloatField()),
                ('ano', models.DateField()),
                ('id_escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EducaUB.tb_escola')),
            ],
        ),
    ]
