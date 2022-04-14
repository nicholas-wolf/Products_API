from django.urls import path
from . import views

urlpatterns = [
    path('<int:fk>/', views.review_table),
    # path('<int:pk>/', views.product_detail)
] 

