# Generated by Django 3.1.6 on 2021-02-10 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlUsuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValoracionMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altura', models.CharField(max_length=50)),
                ('peso', models.CharField(max_length=50)),
                ('enfermedad', models.CharField(max_length=150)),
                ('alergia', models.CharField(max_length=150)),
                ('operaciones', models.CharField(max_length=150)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlUsuarios.usuario')),
            ],
        ),
    ]
