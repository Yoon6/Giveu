from django.urls import path
from . import views


urlpatterns = [
    path('', views.funding_list, name="funding_list"),
    path('create/', views.funding_create, name="funding_create"),
    path('<int:funding_id>/', views.funding_detail, name="funding_detail"),
    path('<int:funding_id>/update/', views.funding_update, name="funding_update"),
    path('<int:funding_id>/delete/', views.funding_delete, name="funding_delete"),

    path('fundingCounter/', views.funding_counter, name="count"), # 펀딩 버튼 눌렀을 때 funding count 1 증가
]