from django.urls import path
from . import views



urlpatterns = [
    path("", views.product_list, name="product_list"),  
    path("category/<slug:category_slug>/", views.product_list, name="product_list_by_category"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path('search/', views.product_search, name='product_search'),
    path('api/products/', views.ProductListAPI.as_view(), name='api_product_list'),
    path('api/products/<int:pk>/', views.ProductDetailAPI.as_view(), name='api_product_detail'),
    path('api/products/<int:product_id>/reviews/', views.ReviewListCreateAPI.as_view(), name='api_product_reviews'),


]

