# Generated by Django 3.2.8 on 2021-10-22 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PedigreePerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='Date Entered')),
                ('person_choice', models.CharField(choices=[(0, 'Grandmother on Parent #1 Side'), (1, 'Grandfather on Parent #1 Side'), (3, 'Sibling of Parent 1'), (4, 'Sibling 2 of Parent 1'), (5, 'Parent 1'), (2, 'Parent 2'), (6, 'Child of Parent 1 & Parent 2'), (7, 'Child 2 of Parent 1 & Parent 2'), (8, 'Child 3 of Parent 1 & Parent 2')], default=0, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PersonInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_age', models.IntegerField(default=0)),
                ('patient_sex', models.CharField(choices=[(0, 'Male'), (1, 'Female')], default=0, max_length=200)),
                ('patient_dna_dx', models.CharField(choices=[(0, 'Known and Undiagnosed'), (1, 'Known and Confirmed Diagnosis'), (9, 'Unkown')], default=0, max_length=200)),
                ('patient_ldlc', models.IntegerField(default=0)),
                ('patient_totc', models.IntegerField(default=0)),
                ('patient_tx', models.CharField(choices=[(0, 'Known and Undiagnosed'), (1, 'Known and Confirmed Diagnosis'), (9, 'Unkown')], default=0, max_length=200)),
                ('patient_clincad_status', models.CharField(choices=[(0, 'Known and Undiagnosed'), (1, 'Known and Confirmed Diagnosis'), (9, 'Unkown')], default=0, max_length=200)),
                ('patient_clincad_age', models.IntegerField(default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fhcalc.pedigreeperson')),
            ],
        ),
    ]
