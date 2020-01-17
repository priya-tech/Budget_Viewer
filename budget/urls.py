from django.urls import path
from . import views

urlpatterns = [
    path('', views.day_view, name='dayviews'),
    path('addincome', views.add_income, name='add_incomes'),
    path('addexpense', views.add_expense, name='add_expenses'),
    path('monthview', views.month_view, name='monthviews'),
    path('yearview', views.year_view, name='yearviews'),
]
