# Generated by Django 5.2.3 on 2025-06-18 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Denuncias', '0005_alter_denuncia_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('resolvido', 'Resolvido')], default='pendente', max_length=20),
        ),
    ]
