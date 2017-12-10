# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-09 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='Nome do Paciente')),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='Nome do Procedimento')),
                ('description', models.CharField(default='', max_length=200, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Procedimento',
                'verbose_name_plural': 'Procedimentos',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(default='', max_length=200, verbose_name='Detalhes')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Patient')),
                ('procedure', models.ManyToManyField(to='schedule.Procedure')),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
            },
        ),
    ]
