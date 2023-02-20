from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as f:
        lst = []
        reader = csv.DictReader(f)
        for line in reader:
            lst.append({'Name': line['Name'], 'Street': line['Street'], 'District': line['District']})

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(lst, 10)
    page = paginator.get_page(page_number)

    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
