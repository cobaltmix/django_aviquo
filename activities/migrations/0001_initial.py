# Generated by Django 4.2.5 on 2024-07-31 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Extracurricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='images/')),
                ('url', models.URLField()),
                ('year', models.CharField(choices=[('9th', '9th grade'), ('10th', '10th grade'), ('11th', '11th grade'), ('12th', '12th grade')], max_length=4)),
                ('cost', models.CharField(choices=[('Free', 'Free'), ('Paid', 'Paid')], max_length=4)),
                ('effort', models.CharField(choices=[('Low', 'Low effort'), ('Medium', 'Medium effort'), ('High', 'High effort'), ('Hypercompetitive', 'Hypercompetitive')], max_length=16)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.subject')),
            ],
        ),
    ]
