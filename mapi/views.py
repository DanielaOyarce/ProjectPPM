from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
import openpyxl

from mapi.models import Mapi
from aircraft.models import Aircraft, Fleet, Operator


def form_mapi(request):
    if request.method=='POST':
        data=request.FILES['archivo']
        workbook = openpyxl.load_workbook(filename=data, use_iterators=True)
        worksheet = workbook.get_sheet_by_name('Hoja1')
        for row in worksheet.iter_rows():
            data = {
                    'Col_1': row[0].value,
                    'Col_2': row[1].value,
                    'Col_3': row[2].value,
                    'col_4': row[3].value,
                    'col_5': row[4].value,
                    'col_6': row[5].value,
                    'col_7': row[6].value,
                    'col_8': row[7].value,
                    'col_9': row[8].value,
                    'col_10': row[9].value,
                    'col_11': row[10].value,
                    'col_12': row[11].value,
                    'col_13': row[12].value,
                    'col_14': row[13].value,
                    'col_15': row[14].value,
                    'col_16': row[15].value,
                    'col_17': row[16].value,
                    'col_18': row[17].value,
                    'col_19': row[18].value,
                    'col_20': row[19].value,
                    }

            fl, created = Fleet.objects.get_or_create(name=data['Col_1'],
                  defaults = {})

            ac, created = Aircraft.objects.get_or_create(name=data['Col_2'],
                  defaults = {'fleet':fl})

            #op, created = Operator.objects.get_or_create(name=data['Col_1'],
            #      defaults={}) 
            if created:
                comment = 'Ingresar Operador %s' % (ac)
                messages.error(request, comment)

            ata = data['Col_3']
            subAta = data['col_4']
            week = data['col_5'] 
            nmfl = data['col_6'] 
            dtlmfl = data['col_7']  
            flightNumber = data['col_8'] 
            sta = data['col_9']  
            referenceTerm = data['col_10']            
            nri = data['col_11']
            dmi = data['col_12'] 
            cat = data['col_13']  
            dueDate = data['col_14']
            discrepancies = data['col_15'] 
            actionCorrect = data['col_16'] 
            partNumber = data['col_17'] 
            position = data['col_18'] 
            status = data['col_19']
            foundOnDate = data['col_20']   
            m = Mapi(aircraft=ac,ata=ata,subAta=subAta,week=week,nmfl=nmfl,dtlmfl=dtlmfl,flightNumber=flightNumber,sta=sta,referenceTerm=referenceTerm,nri=nri,dmi=dmi,cat=cat,dueDate=dueDate,discrepancies=discrepancies,actionCorrect=actionCorrect,partNumber=partNumber,position=position,status=status,foundOnDate=foundOnDate)
            m.save()
    return render(request,'form_mapi.html')

