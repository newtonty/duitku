# Generated by Django 4.0.3 on 2022-03-15 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_rename_voter_username_upvoter_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.post'),
        ),
        migrations.AlterField(
            model_name='upvoter',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.post'),
        ),
    ]
