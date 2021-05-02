from django.contrib import admin
from django.urls import path, include
from advisor_api.views import AdvisorView, RegisterUser, LoginUser, GetAdvisor, BookAdvisor

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/advisor/', AdvisorView.as_view()),
    path('user/register/', RegisterUser.as_view()),
    path('user/login/', LoginUser.as_view()),
    path('user/<id>/advisor/', GetAdvisor.as_view()),
    path('user/<user_id>/advisor/<adv_id>/', BookAdvisor.as_view()),
  ]
