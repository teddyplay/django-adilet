# Generated by Django 4.1.1 on 2022-09-13 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('create_date', models.TimeField(auto_now_add=True)),
                ('update_date', models.TimeField(auto_now=True)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_comment', to='shows.book_detail')),
            ],
        ),
    ]
