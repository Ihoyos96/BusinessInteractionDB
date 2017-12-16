# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
    cid = models.AutoField(db_column='CID', primary_key=True)  # Field name made lowercase.
    salutation = models.CharField(db_column='Salutation', max_length=15, blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=50)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=50)  # Field name made lowercase.
    employer = models.CharField(db_column='Employer', max_length=50)  # Field name made lowercase.
    job_title = models.CharField(db_column='Job_Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manager = models.IntegerField(db_column='Manager', blank=True, null=True)  # Field name made lowercase.
    secretary = models.IntegerField(db_column='Secretary', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
	    return "CID: " + str(self.cid) + "Name: " + str(self.first_name) + " " + str(self.last_name)

    class Meta:
        managed = False
        db_table = 'Contact'


class ContactAddress(models.Model):
    cid = models.ForeignKey(Contact, models.DO_NOTHING, db_column='CID')  # Field name made lowercase.
    home = models.CharField(db_column='Home', max_length=255, blank=True, null=True)  # Field name made lowercase.
    office = models.CharField(db_column='Office', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    caid = models.AutoField(db_column='CAID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contact_Address'

    def __str__(self):
	    return "CID: " + str(self.cid)


class Department(models.Model):
    did = models.AutoField(db_column='DID', primary_key=True)  # Field name made lowercase.
    department_name = models.CharField(db_column='Department_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
	    return "DID: " + str(self.did) + " " + str(self.department_name)

    class Meta:
        managed = False
        db_table = 'Department'


class Employee(models.Model):
    eid = models.AutoField(db_column='EID', primary_key=True)  # Field name made lowercase.
    did = models.ForeignKey(Department, models.DO_NOTHING, db_column='DID')  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=50)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=50)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    job_title = models.CharField(db_column='Job_Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manager = models.IntegerField(db_column='Manager', blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary')  # Field name made lowercase.

    def __str__(self):
	    return "EID: " + str(self.eid) + " Name: " +str(self.first_name) + " " + str(self.last_name)

    class Meta:
        managed = False
        db_table = 'Employee'


class Interactions(models.Model):
    iid = models.AutoField(db_column='IID', primary_key=True)  # Field name made lowercase.
    cid = models.ForeignKey(Contact, models.DO_NOTHING, db_column='CID')  # Field name made lowercase.
    eid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EID')  # Field name made lowercase.
    business_name = models.CharField(db_column='Business_Name', max_length=50)  # Field name made lowercase.
    medium = models.CharField(db_column='Medium', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
	    return "IID: " + str(self.iid) + "Business: " +str(self.business_name)

    class Meta:
        managed = False
        db_table = 'Interactions'


class PhoneInfo(models.Model):
    cid = models.ForeignKey(Contact, models.DO_NOTHING, db_column='CID')  # Field name made lowercase.
    home = models.CharField(db_column='Home', max_length=15, blank=True, null=True)  # Field name made lowercase.
    office = models.CharField(db_column='Office', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cellular = models.CharField(db_column='Cellular', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=15, blank=True, null=True)  # Field name made lowercase.
    secretary = models.CharField(db_column='Secretary', max_length=15, blank=True, null=True)  # Field name made lowercase.
    piid = models.AutoField(db_column='PIID', primary_key=True)  # Field name made lowercase.

    def __str__(self):
	    return "CID: " + str(self.cid)

    class Meta:
        managed = False
        db_table = 'Phone_Info'









