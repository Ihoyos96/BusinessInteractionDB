# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django_tables2 import RequestConfig

from .models import Employee, Contact, Interactions
from .tables import contactsTable, interactionsTable

from datetime import datetime

# Create your views here.

def search(request, search_id):
    return HttpResponse("Search Page %s." % search_id)


"""def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")"""

#def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
       # 'latest_question_list': latest_question_list,
    
    #return render(request, 'BusComm/index.html')
def index(request):
    return render(request, 'BusComm/title.html')
   

def contacts(request):
    results=None
    if request.GET.get('cid'):
        query_cid = request.GET.get('cid')

    	table = contactsTable(Contact.objects.filter(cid=query_cid))
    	return render(request, 'BusComm/contacts.html',{
        'results': results, 'table': table,
    })
    
    if request.GET.get('first_name', 'last_name'):
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')

    	table = contactsTable(Contact.objects.filter(first_name=first_name, last_name=last_name))
    	return render(request, 'BusComm/contacts.html',{
        'results': results, 'table': table,
    })

    if request.GET.get('first_name'):
        first_name = request.GET.get('first_name')

    	table = contactsTable(Contact.objects.filter(first_name=first_name))
    	return render(request, 'BusComm/contacts.html',{
        'results': results, 'table': table,
    })


    if request.GET.get('last_name'):
        last_name = request.GET.get('last_name')

    	table = contactsTable(Contact.objects.filter(last_name=last_name))
    	return render(request, 'BusComm/contacts.html',{
        'results': results, 'table': table,
    	})

    if request.GET.get('employer'):
        employer = request.GET.get('employer')

    	table = contactsTable(Contact.objects.filter(employer=employer))
    
    	return render(request, 'BusComm/contacts.html',{
        'results': results, 'table': table,
    })

    if request.GET.get('first_name', 'employer'):
        first_name = request.GET.get('first_name')
        employer = request.GET.get('employer')

    	table = contactsTable(Contact.objects.filter(first_name=first_name, employer=employer))
    
    	return render(request, 'BusComm/contacts.html',{
        'results': results, 'table': table,
    })

    if request.GET.get('last_name', 'employer'):
        last_name = request.GET.get('last_name')
        employer = request.GET.get('employer')

    	table = contactsTable(Contact.objects.filter(last_name=last_name, employer=employer))
    	return render(request, 'BusComm/contacts.html',{
        'results': results, 'table': table,
    })
    return render(request, 'BusComm/contacts.html',{
        'results': results, 'table': table,
    })


def interactions(request):
	today = datetime.now().date()
	table = interactionsTable(Interactions.objects.all())

    	if request.GET.get('cid'):
            query_cid = request.GET.get('cid')

            table = interactionsTable(Interactions.objects.filter(cid=query_cid))
            return render(request, 'BusComm/interactions.html',{
                 'table': table,
            })

        if request.GET.get('medium'):
            medium = request.GET.get('medium')

            table = interactionsTable(Interactions.objects.filter(medium=medium))
            return render(request, 'BusComm/interactions.html',{
                'table': table,
            })

        if request.GET.get('employer'):
            employer = request.GET.get('employer')

            table = interactionsTable(Interactions.objects.filter(business_name=employer))
            return render(request, 'BusComm/interactions.html',{
                'table': table,
            })

        if request.GET.get('employer', 'medium'):
            employer = request.GET.get('employer')
            medium = request.GET.get('medium')

            table = interactionsTable(Interactions.objects.filter(business_name=employer, medium=medium))
            return render(request, 'BusComm/interactions.html',{
                'table': table,
            })

        if request.GET.get('date_from'):
            date_from = request.GET.get('date_from')

            table = interactionsTable(Interactions.objects.filter(date__range=[date_from, today]))
            return render(request, 'BusComm/interactions.html',{
                'table': table,
            })

        if request.GET.get('date_from', 'date_to', 'employer'):
            date_from = request.GET.get('date_from')
            date_to = request.GET.get('date_to')
            employer = request.GET.get('employer')

            table = interactionsTable(Interactions.objects.filter(date__range=[date_from, date_to], business_name=employer,))
            return render(request, 'BusComm/interactions.html',{
                'table': table,
            })

        if request.GET.get('date_from', 'date_to'):
            date_from = request.GET.get('date_from')
            date_to = request.GET.get('date_to')

            table = interactionsTable(Interactions.objects.filter(date__range=[date_from, date_to]))
            return render(request, 'BusComm/interactions.html',{
                'table': table,
            }) 

	return render(request, 'BusComm/interactions.html',{
	        'table': table,
	    })



def search_employees(request):
	query = request.GET.get('q')
	try:
		query = int(query)
	except ValueError:
		query = None
		results = None
	if query:
		results = Employee.objects.filter(eid=query).values()
	return render(request, 'BusComm/results.html', {'results': results})





