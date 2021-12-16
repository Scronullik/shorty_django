# Generated by Django 4.0 on 2021-12-15 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shorty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subpart', models.CharField(max_length=10)),
                ('url', models.URLField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('session', models.ForeignKey(db_column='session_key', on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
            ],
        ),
    ]