import django_tables2 as tables
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .models import Contact, Interactions

class contactsTable(tables.Table):
    class Meta:
        model = Contact
        template = 'django_tables2/bootstrap.html'


class interactionsTable(tables.Table):
    class Meta:
        model = Interactions
        template = 'django_tables2/bootstrap.html'