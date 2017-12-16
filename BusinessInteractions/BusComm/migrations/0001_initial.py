# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('cid', models.AutoField(db_column='CID', primary_key=True, serialize=False)),
                ('salutation', models.CharField(blank=True, db_column='Salutation', max_length=15, null=True)),
                ('first_name', models.CharField(db_column='First_Name', max_length=50)),
                ('last_name', models.CharField(db_column='Last_Name', max_length=50)),
                ('employer', models.CharField(db_column='Employer', max_length=50)),
                ('job_title', models.CharField(blank=True, db_column='Job_Title', max_length=50, null=True)),
                ('manager', models.IntegerField(blank=True, db_column='Manager', null=True)),
                ('secretary', models.IntegerField(blank=True, db_column='Secretary', null=True)),
                ('comments', models.CharField(blank=True, db_column='Comments', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Contact',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContactAddress',
            fields=[
                ('home', models.CharField(blank=True, db_column='Home', max_length=255, null=True)),
                ('office', models.CharField(blank=True, db_column='Office', max_length=255, null=True)),
                ('mail', models.CharField(blank=True, db_column='Mail', max_length=255, null=True)),
                ('caid', models.AutoField(db_column='CAID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Contact_Address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('did', models.AutoField(db_column='DID', primary_key=True, serialize=False)),
                ('department_name', models.CharField(blank=True, db_column='Department_Name', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.AutoField(db_column='EID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_column='First_Name', max_length=50)),
                ('last_name', models.CharField(db_column='Last_Name', max_length=50)),
                ('sex', models.CharField(db_column='Sex', max_length=1)),
                ('dob', models.DateField(db_column='DOB')),
                ('job_title', models.CharField(blank=True, db_column='Job_Title', max_length=50, null=True)),
                ('manager', models.IntegerField(blank=True, db_column='Manager', null=True)),
                ('email_address', models.CharField(blank=True, db_column='Email_Address', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('salary', models.IntegerField(db_column='Salary')),
            ],
            options={
                'db_table': 'Employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Interactions',
            fields=[
                ('iid', models.AutoField(db_column='IID', primary_key=True, serialize=False)),
                ('business_name', models.CharField(db_column='Business_Name', max_length=50)),
                ('medium', models.CharField(blank=True, db_column='Medium', max_length=50, null=True)),
                ('date', models.DateTimeField(db_column='Date', verbose_name=['%m-%d-%Y %H:%M:%S'])),
                ('comments', models.CharField(blank=True, db_column='Comments', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Interactions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PhoneInfo',
            fields=[
                ('home', models.CharField(blank=True, db_column='Home', max_length=15, null=True)),
                ('office', models.CharField(blank=True, db_column='Office', max_length=15, null=True)),
                ('cellular', models.CharField(blank=True, db_column='Cellular', max_length=15, null=True)),
                ('fax', models.CharField(blank=True, db_column='Fax', max_length=15, null=True)),
                ('secretary', models.CharField(blank=True, db_column='Secretary', max_length=15, null=True)),
                ('piid', models.AutoField(db_column='PIID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Phone_Info',
                'managed': False,
            },
        ),
    ]