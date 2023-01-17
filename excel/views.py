from datetime import datetime, date
import xlwt
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from lottery.models import SalePlan


def Export_SalePlan_Excel(request):
    today_date = date.today()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="saleplans' + str(today_date) + '.xls"'
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('لیست طرح های فروش')
    columns = ['طرح', 'تاریخ شزوع ثبت نام', 'تاریخ پایان ثبت نام', 'تاریخ قرعه کشی']
    rowNumber = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for column in range(len(columns)):
        worksheet.write(rowNumber, column, columns[column], font_style)

    salePlans = SalePlan.objects.all().values_list("Description", "RegisterStartDate")

    for salePlan in salePlans:
        rowNumber += 1

        for column in range(len(salePlan)):
            worksheet.write(rowNumber, column, salePlan[column])

    workbook.save(response)

    return response
