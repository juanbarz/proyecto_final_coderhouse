# Generated by Django 4.2.2 on 2023-07-01 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tblog_app', '0011_alter_comentarios_articulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='articulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='tblog_app.articulo'),
        ),
    ]
