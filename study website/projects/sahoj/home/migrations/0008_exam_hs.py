# Generated by Django 3.1 on 2020-10-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_hs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Questions', models.ImageField(default='', upload_to='home/images2')),
                ('option1', models.CharField(default='', max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('correctAns', models.CharField(max_length=100)),
                ('questionNO', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
