from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # these items will be set as args from get_absolute_url() method.
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail')
]