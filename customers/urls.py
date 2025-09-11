from django.urls import path
from .views import CustomerListView , CustomerDetailView  , register , profile_detail , profile_edit
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('<int:pk>/',CustomerDetailView.as_view(), name='customer_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='customers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    path('profile/' , profile_detail , name='profile_detail'),
    path('profile/edit' , profile_edit , name='profile_edit')
    
]
