# Generated by Django 5.2.1 on 2025-05-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Denuncias', '0002_alter_denuncia_responsavel_delete_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagens/'),
        ),
    ]
