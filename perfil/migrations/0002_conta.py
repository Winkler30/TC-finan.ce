# Generated by Django 5.0.6 on 2024-06-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=50)),
                ('banco', models.CharField(choices=[('NU', 'Nubank'), ('IT', 'Itaú'), ('BB', 'Banco do Brasil'), ('BR', 'Bradesco'), ('SA', 'Santander'), ('CA', 'Caixa Econômica Federal'), ('ME', 'Mercado Bitcoin'), ('OT', 'Outro')], max_length=2)),
                ('tipo', models.CharField(choices=[('pf', 'Pessoa Física'), ('pj', 'Pessoa Jurídica')], max_length=2)),
                ('valor', models.FloatField()),
                ('icone', models.ImageField(upload_to='icones')),
            ],
        ),
    ]
