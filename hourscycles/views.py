from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum, Count
from django.db import connection
from datetime import datetime
from dateutil.relativedelta import relativedelta

import xlrd
import datetime as dt
import time
import string
import pytz
import sys
import os

from hourscycles.models import Hourscycles
from aircraft.models import Aircraft, Fleet, Operator
from mapi.models import Mapi



class HomeView(TemplateView):
    template_name = "hourscycles/index.html"


def ReportView(request):
    return render(request, "hourscycles/graph.html")


def date_default(date):
    dd = date.split("-")                    
    d1 = dt.date(int(dd[0]),int(dd[1]),int(dd[2]))
    d2 = d1.replace(day=01)
    return d2


def UploadHoursCyclesView(request):
    if request.method == 'POST':
        data = request.FILES['archivo']
        date = request.POST['date']
        workbook = xlrd.open_workbook(file_contents=data.read())
        sheet = workbook.sheet_by_index(0)

        if sheet.ncols == 9:
            for rx in range(1, sheet.nrows):
                rows = sheet.row_values(rx)

                if sheet.cell_type(rx, 1) != 0:
                    fleet, created = Fleet.objects.get_or_create(name=rows[0])
                    aircraft, created = Aircraft.objects.get_or_create(name=rows[1], 
                        defaults={'fleet': fleet})  

                    new_date = date_default(date)

                    # Save Hourscycles
                    hourscycles, created = Hourscycles.objects.update_or_create(aircraft=aircraft, date=new_date, 
                      defaults={ 
						'flight_hours': rows[2],
						'block_hours': rows[3],
						'cycles': rows[4], 
						'tsn': rows[5], 
						'csn': rows[6], 
						'nonrevenue_cycles': rows[7], 
						'days_flown': rows[8],
                      })
    return render(request,'hourscycles/form_hourscycles.html')


def utilization(request):
    fl = Fleet.objects.all()
    op = Operator.objects.all()
    if request.method == 'POST':
        date = request.POST['date']
        fleet_ut = request.POST['fleet']
        #operator = request.POST['operator']
        
        month = date.split('-')

        fh = Hourscycles.objects.filter(aircraft__fleet__name=fleet_ut, date=date, aircraft__name__startswith='CC').exclude(aircraft__name='CC-CZZ').aggregate(Sum('flight_hours'))
        take_off = Hourscycles.objects.filter(aircraft__fleet__name=fleet_ut, date=date, aircraft__name__startswith='CC').exclude(aircraft__name='CC-CZZ').aggregate(Sum('cycles'))
        no_revenue_cycles = Hourscycles.objects.filter(aircraft__fleet__name=fleet_ut, date=date, aircraft__name__startswith='CC').exclude(aircraft__name='CC-CZZ').aggregate(Sum('nonrevenue_cycles'))
        t_o_re = take_off['cycles__sum']-no_revenue_cycles['nonrevenue_cycles__sum']
        tt_ac = Hourscycles.objects.filter(aircraft__fleet__name=fleet_ut, date=date, aircraft__name__startswith='CC').exclude(aircraft__name='CC-CZZ').aggregate(Count('nonrevenue_cycles'))
        q_report = Mapi.objects.filter(aircraft__fleet__name=fleet_ut, found_on_date__month=month[1], aircraft__name__startswith='CC').aggregate(Count('aircraft_id'))

       
        data = {
            'fh':fh['flight_hours__sum'],
            'take_off':take_off['cycles__sum'],
            'no_revenue_cycles':no_revenue_cycles['nonrevenue_cycles__sum'],
            't_o_re':t_o_re,
            'tt_ac':tt_ac['nonrevenue_cycles__count'],
            'q_report':q_report['aircraft_id__count'],
            'date':date,
            'fleet_ut':fleet_ut,            
            'fl':fl,
            'op':op,
        }

        return render(request,'hourscycles/utilization.html', data)


    data = {
            'fl':fl,
            'op':op,
           }

    #mostrar tabla con datos solicitados
    return render(request,'hourscycles/utilization.html', data)


def GetDic(query):
    cursor = connection.cursor()
    cursor.execute(query)
    qury_row = cursor.fetchall()
    x = cursor.description
    diccionary = []
    for r in qury_row:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i += 1
            diccionary.append(d)              
    return diccionary


def graphics_utilization(request):
    fl = Fleet.objects.all()
    op = Operator.objects.all()
    if request.method == 'POST':
        date = request.POST['date']
        fleet_ut = request.POST['fleet']
     
        query = "SELECT DISTINCT aircraft_aircraft.id, aircraft_aircraft.name AS aircraft, aircraft_aircraft.fleet_id, aircraft_fleet.name, aircraft_fleet.id,hourscycles_hourscycles.aircraft_id, hourscycles_hourscycles.date, hourscycles_hourscycles.flight_hours, hourscycles_hourscycles.days_flown, hourscycles_hourscycles.flight_hours/hourscycles_hourscycles.days_flown AS Utilidad FROM aircraft_aircraft, aircraft_fleet, hourscycles_hourscycles WHERE   aircraft_aircraft.fleet_id=aircraft_fleet.id AND hourscycles_hourscycles.aircraft_id=aircraft_aircraft.id AND hourscycles_hourscycles.date='"+ date +"' AND aircraft_fleet.name='"+ fleet_ut +"' AND aircraft_aircraft.name like 'CC%' GROUP BY aircraft_aircraft.name ORDER BY aircraft_aircraft.name ASC"
        items = GetDic(query)

        data = {
            'items':items,
            'date':date,
            'fleet_ut':fleet_ut,
            'fl':fl,
            'op':op,
            }
        return render(request,'hourscycles/graphics_utilization.html', data)
    data = {                    
            'fl':fl,
            'op':op,
            }

    return render(request,'hourscycles/graphics_utilization.html', data)


def rate_pireps(request):
    fl = Fleet.objects.all()
    if request.method == 'POST':
        date_from = request.POST['date_from']
        date_to = request.POST['date_to']
        fleet_ut = request.POST['fleet']

        month = date_from.split('-')

        #format_date = date_to.strftime("%Y-%m")

        fh = Hourscycles.objects.filter(aircraft__fleet__name=fleet_ut, date__month=month[1], aircraft__name__startswith='CC').exclude(aircraft__name='CC-CZZ').aggregate(Sum('flight_hours'))
        print fh

        query = "SELECT *, count(ata) AS contar  FROM mapi_mapi, aircraft_aircraft, aircraft_fleet WHERE mapi_mapi.aircraft_id = aircraft_aircraft.id AND aircraft_fleet.id = aircraft_aircraft.fleet_id AND aircraft_fleet.name ='"+ fleet_ut +"' AND mapi_mapi.found_on_date >='"+ date_from +"' AND mapi_mapi.found_on_date <= '"+ date_to +"' AND mapi_mapi.reference_term='PIREP' AND mapi_mapi.ata >= 21 AND mapi_mapi.ata <= 80 AND aircraft_aircraft.name LIKE 'CC%' GROUP BY ata ORDER BY ata"
        items = GetDic(query)

        pirep = []
        for i in items:
            calculo = (i['contar']/fh['flight_hours__sum'])*1000
            pirep.append((calculo, i['ata'], date_from)) 

        data = {
            'fh':fh['flight_hours__sum'],
            'pirep':pirep,
            'date_from':date_from,
            'date_to':date_to,
            'fleet_ut':fleet_ut,
            'items':items,
            'fl':fl,
        }

        return render(request,'hourscycles/rate_pireps.html', data)

    data = {'fl':fl}
    return render(request,'hourscycles/rate_pireps.html', data)