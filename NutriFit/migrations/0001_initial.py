# Generated by Django 3.1 on 2021-01-07 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('calorias', models.IntegerField()),
                ('verificado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Composta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NutriFit.alimento')),
            ],
        ),
        migrations.CreateModel(
            name='Macronutrientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hidratos_carbono', models.DecimalField(decimal_places=1, default='', max_digits=4)),
                ('proteina', models.DecimalField(decimal_places=1, default='', max_digits=4)),
                ('gordura', models.DecimalField(decimal_places=1, default='', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Refeicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('data', models.DateField()),
                ('alimentos', models.ManyToManyField(through='NutriFit.Composta', to='NutriFit.Alimento')),
                ('utilizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('altura', models.IntegerField(blank=True, null=True)),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, max_length=20, null=True)),
                ('objetivo', models.CharField(blank=True, max_length=20, null=True)),
                ('imc', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('ci', models.IntegerField(blank=True, null=True)),
                ('atividade', models.CharField(blank=True, max_length=40, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='composta',
            name='refeicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NutriFit.refeicao'),
        ),
        migrations.AddField(
            model_name='alimento',
            name='categoria',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='NutriFit.categoria'),
        ),
        migrations.AddField(
            model_name='alimento',
            name='macro_nutrientes',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='NutriFit.macronutrientes'),
        ),
    ]
