from django.urls import path
from .views import generate_excel_report

urlpatterns = [
    # ...
    path('api/download_excel_report/', generate_excel_report, name='download_excel_report'),
    # ...
]
