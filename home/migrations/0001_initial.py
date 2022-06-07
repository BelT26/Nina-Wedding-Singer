# Generated by Django 3.2.13 on 2022-05-31 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('artist', models.CharField(max_length=300)),
                ('playlist', models.CharField(choices=[('CE', 'Ceremony'), ('EV', 'Evening')], default='EV', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('paragraph1', models.TextField()),
                ('paragraph2', models.TextField()),
                ('paragraph3', models.TextField()),
                ('paragraph4', models.TextField()),
                ('paragraph5', models.TextField()),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
