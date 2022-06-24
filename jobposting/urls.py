from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('jobposting-list/', views.jobpostingList, name="jobposting-list"),
    path('jobposting-detail/<str:pk>/', views.jobpostingDetail, name="jobposting-detail"),
    path('jobposting-create/', views.jobpostingCreate, name="jobposting-create"),
    path('jobposting-update/<str:pk>/', views.jobpostingUpdate, name="jobposting-update"),
    path('jobposting-delete/<str:pk>/', views.jobpostingDelete, name="jobposting-delete"),
]
