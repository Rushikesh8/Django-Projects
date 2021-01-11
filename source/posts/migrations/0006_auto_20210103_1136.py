# Generated by Django 2.2.5 on 2021-01-03 06:06

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210102_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='next_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='posts.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='previous_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous', to='posts.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
