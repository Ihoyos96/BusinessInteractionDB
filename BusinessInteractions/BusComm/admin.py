# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Department, Employee, Contact, ContactAddress, PhoneInfo, Interactions


# Register your models here.

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Contact)
admin.site.register(ContactAddress)
admin.site.register(PhoneInfo)
admin.site.register(Interactions)