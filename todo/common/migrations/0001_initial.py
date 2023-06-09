# Generated by Django 4.2 on 2023-04-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('priority', models.CharField(choices=[('LOW', 'LOW'), ('MIDDLE', 'MIDDLE'), ('HIGH', 'HIGH')], default='LOW', max_length=6)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
