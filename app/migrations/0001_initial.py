# Generated by Django 5.0.3 on 2024-03-26 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaSaber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='InstituicaoEnsino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('site', models.URLField(blank=True)),
                ('telefone', models.CharField(blank=True, max_length=20)),
                ('cidade', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PeriodoCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('pai', models.CharField(blank=True, max_length=255)),
                ('mae', models.CharField(blank=True, max_length=255)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cidade', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('carga_horaria_total', models.IntegerField()),
                ('duracao_meses', models.IntegerField()),
                ('area_saber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areasaber')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicaoensino')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('area_saber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areasaber')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('data_avaliacao', models.DateField()),
                ('tipo_avaliacao', models.CharField(choices=[('Prova', 'Prova'), ('Trabalho', 'Trabalho'), ('Apresentação', 'Apresentação')], max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_previsao_termino', models.DateField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicaoensino')),
                ('periodo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.periodocurso')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matriculas', to='app.pessoa')),
            ],
        ),
    ]
