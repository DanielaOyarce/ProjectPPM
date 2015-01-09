from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum, Count
from django.db import connection
from datetime import datetime,date

import xlrd
import datetime as dt
import calendar

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


def add_months(new_date_to,months):
    month = new_date_to.month - 1 + months
    year = new_date_to.year + month / 12
    month = month % 12 + 1
    day = min(new_date_to.day,calendar.monthrange(year,month)[1])
    return dt.date(year,month,day)


def rest_months(new_date_to,months):
    month = new_date_to.month - 1 + months
    year = new_date_to.year + month / 12
    month = month % 12 + 1
    day = min(new_date_to.day,calendar.monthrange(year,month)[1])
    return dt.date(year,month,day)


def ratepirep_calculate(count, flight_hours):
    calculation = (count/flight_hours)*1000
    return calculation


def rate_pireps(request):
    fl = Fleet.objects.all()
    d = []
    pirep = []
    rate = []
    ata = []
    atas = []
    atas = [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,49,51,52,53,54,55,56,57,71,72,73,74,75,76,77,78,79,80]
    new_list = []
    date_rate = []

    if request.method == 'POST':
        date_from = request.POST['date_from']
        date_to = request.POST['date_to']
        fleet_ut = request.POST['fleet']

        new_date_from = datetime.strptime(date_from,'%Y-%m-%d')
        months = 1
        while months <= 12:
            new_month = add_months(new_date_from, months)
            month_from = new_month.month
            year_from = new_month.year
                               
            fh = Hourscycles.objects.filter(aircraft__fleet__name=fleet_ut, date__month=month_from, date__year=year_from, aircraft__name__startswith='CC')\
                        .exclude(aircraft__name='CC-CZZ')\
                        .order_by('month_from')\
                        .aggregate(Sum('flight_hours'))
            rate.append((fh,month_from,year_from))
            d.append(new_month.strftime("%b-%Y"))
            months += 1 
        
        #print rate, '\n'

        query = "SELECT DISTINCT ata,date_format(found_on_date,'%Y-%m') AS fecha,count(ata) AS contar FROM mapi_mapi, aircraft_aircraft, aircraft_fleet WHERE mapi_mapi.aircraft_id = aircraft_aircraft.id AND aircraft_fleet.id = aircraft_aircraft.fleet_id AND aircraft_fleet.name ='"+ fleet_ut +"' AND mapi_mapi.found_on_date >='"+ date_from +"' AND mapi_mapi.found_on_date <= '"+ date_to +"' AND mapi_mapi.reference_term='PIREP' AND mapi_mapi.ata >= 21 AND mapi_mapi.ata <= 80 AND aircraft_aircraft.name LIKE 'CC%' AND aircraft_aircraft.name NOT LIKE 'CC-CZZ' GROUP BY mapi_mapi.ata, date_format(found_on_date,'%Y-%m') ORDER BY ata, date_format(found_on_date,'%Y-%m') ASC"
        
        items = GetDic(query)
      
        for j in items:
            ata.append(j['ata'])

        dates = []
        for f in items:
            fech = datetime.strptime(f['fecha'],'%Y-%m').date()
            dates.append(fech)
        # lista de atas sin repetir
        lst = list(set(ata))
        mi_fecha = list(set(dates))
        # Fecha ordenada
        mi_fecha2 = sorted(mi_fecha)

        # lista atas faltantes
        for i in atas:
            if i not in lst:
                new_list.append(i)
            
        for k in rate:
            new_date = date(year=k[2],month=k[1],day=1)
            date_rate.append(new_date)

          # Lista de todas las Atas
        
        for i in items: 
            if i['ata'] in atas and i['fecha'] in date_rate:
                print i['ata'], i['fecha'], i['contar'],"Ata y fecha encontrada"
            else:
                print i['ata'],i['fecha'],"fecha no encontrada"

                    #                        
                    # 
                    #     new_date = date(year=r[2],month=r[1],day=1)
        
        1/0
        print "********"
        
        #for r in rate: #fh, mes, anio
           # new_date = date(year=r[1],month=r[2],day=1)
           # for i in items:
               # a = i['contar'] 
               # b = datetime.strptime(i['fecha'],'%Y-%m').date()  
               # c = i['ata']
            
        # for at in atas:
        #     for f in mi_fecha2:  
        #         for i in items:
        #             if at == i[0] and f == i[1]: 
        #                     print "Dato encontrado"                 
        #                     # result = ratepirep_calculate(a,j['flight_hours__sum'])
        #                     # pirep.append((result,at, b.strftime("%b-%Y")))         
        #             else:
        #                     print "Dato no encomtrado"
        #                     # result = 0
        #                     # pirep.append((result,at, b.strftime("%b-%Y")))  
                   

        #pirep_new = list(set(pirep)) 
        #pirep_new2 = sorted(pirep_new)       

        data = {
            'atas':atas,
            'pirep':pirep,
            'rate':rate,                    
            'date_from':date_from,
            'date_to':date_to,
            'fleet_ut':fleet_ut,
            'items':items,
            'fl':fl,
            'd':d,
        }
        return render(request,'hourscycles/rate_pireps.html', data)
            

    data = {'fl':fl}
    return render(request,'hourscycles/rate_pireps.html', data)