# Generated by Django 4.2 on 2023-04-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='genre',
        ),
        migrations.AlterField(
            model_name='movies',
            name='language',
            field=models.CharField(choices=[('malayalm', 'malayalm'), ('tamil', 'tamil'), ('telungu', 'telungu'), ('english', 'english')], default='malayalm', max_length=200),
        ),
        migrations.AddField(
            model_name='movies',
            name='genre',
            field=models.ManyToManyField(null=True, to='myapp.genres'),
        ),
    ]
