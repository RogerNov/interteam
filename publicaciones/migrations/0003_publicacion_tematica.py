# Generated by Django 2.0.5 on 2018-07-27 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
        ('publicaciones', '0002_publicacion_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='tematica',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='notas.Temas'),
            preserve_default=False,
        ),
    ]