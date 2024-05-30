from django.contrib import admin
from django.urls import path
from agendamento import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.ver_consultas),
    path('deletar_consulta/<int:id>/', views.deletar_consulta, name='deletar_consulta')
]
