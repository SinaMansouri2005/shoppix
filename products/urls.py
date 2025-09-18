from django.urls import path
from . import views



urlpatterns = [
    path("", views.product_list, name="product_list"),  
    path("category/<slug:category_slug>/", views.product_list, name="product_list_by_category"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path('search/', views.product_search, name='product_search'),
    path("discounts/", views.discounted_products_list, name="discounted_products"),
    path("best-selling/", views.best_selling_products_list, name="best_selling_products"),
]

