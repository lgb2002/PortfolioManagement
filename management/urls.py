from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('contact/', views.contact, name='contact'),
	path('home/', views.post_list, name='post_list2'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('admin/', views.admin, name='admin'),
	path('portfolio/', views.portfolio, name='portfolio'),
	path('send/', views.send, name='send'),
	path('data/', views.data, name='data'),
	path('test/', views.test, name='test'),
	path('test2/', views.test2, name='test2'),
	path('contact/post_contact', views.post_contact, name='post_contact'),
]