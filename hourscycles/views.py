from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone

import xlrd
import datetime as dt
import string
import pytz

from hourscycles.models import Hourscycles
from aircraft.models import Aircraft, Fleet, Operator



def form_hourscycles(request):
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

                    dd = date.split("-")                    
                    d1 = dt.date(int(dd[0]),int(dd[1]),int(dd[2]))
                    d2 = d1.replace(day=01)
                    
                    # Save Hourscycles
                    hourscycles, created = Hourscycles.objects.update_or_create(aircraft=aircraft, date=d2, 
                      defaults={ 
						'flight_hours': rows[2],
						'block_hours': rows[3],
						'cycles': rows[4], 
						'tsn': rows[5], 
						'csn': rows[6], 
						'nonrevenue_cycles': rows[7], 
						'days_flown': rows[8],
                      })
    return render(request,'form_hourscycles.html')