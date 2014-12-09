from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone

import xlrd
import datetime as dt
import pytz

from mapi.models import Mapi
from aircraft.models import Aircraft, Fleet, Operator


def DateExcelToPython(workbook, sheet, rx, cell):
    try:
        xldate = sheet.cell_value(rowx=rx, colx=cell)
        tuple_date = xlrd.xldate_as_tuple(xldate, workbook.datemode)
        pydatetime = dt.datetime(*tuple_date)
        return pydatetime
    except Exception, e:
        print e


def form_mapi(request):
    if request.method == 'POST':
        data = request.FILES['archivo']
        workbook = xlrd.open_workbook(file_contents=data.read())
        sheet = workbook.sheet_by_index(0)

        print sheet.name, sheet.nrows, sheet.ncols     
        
        if sheet.ncols == 20:
            for rx in range(1, sheet.nrows):
                rows = sheet.row_values(rx)
                print rows[1]
                
                if sheet.cell_type(rx, 1) != 0:
                    fleet, created = Fleet.objects.get_or_create(name=rows[0])
                    aircraft, created = Aircraft.objects.get_or_create(name=rows[1], 
                        defaults={'fleet': fleet})

                    if rows[6]:
                        dtlmfl = DateExcelToPython(workbook, sheet, rx, 6)
                        print dtlmfl
                    else:
                        dtlmfl = '2000-01-01 00:00:00'
                        print 'Vacio col 6'

                    if rows[13]:
                        duedate = DateExcelToPython(workbook, sheet, rx, 13)
                        print duedate
                    else:
                        duedate = '2000-01-01 00:00:00'
                        print 'Vacio col 13'

                    if rows[19]:
                        found_on_date = DateExcelToPython(workbook, sheet, rx, 19)
                        print found_on_date
                    else:
                        #print 'Error'
                        found_on_date = '2000-01-01 00:00:00'
                        print 'Vacio col 19'

                    # Save Pireps & Mareps
                    mapi, created = Mapi.objects.update_or_create(nri=rows[10], 
                      defaults={
                        'aircraft':aircraft, 
                        'ata':rows[2],
                        'subata':rows[3],
                        'week':rows[4],
                        'nmfl':rows[5],
                        'dtlmfl':dtlmfl,
                        'flight_number':rows[7],
                        'sta':rows[8],
                        'reference_term':rows[9],
                        'dmi':rows[11],
                        'cat':rows[12],
                        'duedate':duedate,
                        'discrepancies':rows[14],
                        'action_correct':rows[15],
                        'part_number':rows[16],
                        'position':rows[17],
                        'status':rows[18],
                        'found_on_date':found_on_date
                      })
    return render(request,'mapi/form_mapi.html')