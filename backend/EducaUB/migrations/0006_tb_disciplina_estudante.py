# Generated by Django 3.1.4 on 2020-12-20 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EducaUB', '0005_tb_administrador_tb_disciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_disciplina_estudante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notas1', models.FloatField()),
                ('notas2', models.FloatField()),
                ('notas3', models.FloatField()),
                ('notas4', models.FloatField()),
                ('faltas', models.IntegerField()),
                ('id_disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EducaUB.tb_disciplina')),
                ('id_estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EducaUB.tb_estudante')),
            ],
        ),
    ]