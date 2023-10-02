from django.http import HttpResponse
from openpyxl import Workbook
from .models import Robot
from datetime import datetime, timedelta


def generate_excel_report(request):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    robots = Robot.objects.filter(created__range=(start_date, end_date))

    wb = Workbook()
    ws = wb.active
    ws.title = "Отчет о роботах"

    ws.append(["Модель", "Версия", "Количество за неделю"])

    for robot in robots:
        ws.append([robot.model, robot.version, robot.quantity])

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=robot_report.xlsx'
    wb.save(response)

    return response
