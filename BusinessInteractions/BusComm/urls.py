from django.conf.urls import url

from . import views

from views import index, search_employees, contacts, interactions
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ex: /polls/
    url(r'^$', index, name='index'),

    url(r'^search_employees$', search_employees, name='search_employees'),

    url(r'^contacts$', contacts, name='contacts'),

    url(r'^interactions$', interactions, name='interactions'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)