from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('map/', views.map_view, name='map'),
    path('add-store/', views.add_store_view, name='add_store'),
    path('edit-stores-list/', views.edit_stores_list_view, name='edit_stores_list'),
    path('delete-stores-list/', views.delete_stores_list_view, name='delete_stores_list'),
    path('search/', views.search_view, name='search'),
    path('edit-store/<int:pk>/', views.edit_store_view, name='edit_store'),
    path('delete-store/<int:pk>/', views.delete_store_view, name='delete_store'),

    path('help/', views.help_view, name='help'),


    path('about/', views.about_view, name='about'),
    path('profile/', views.profile_view, name='profile'),
    path('logout-confirm/', views.logout_confirm_view, name='logout_confirm'),
    path('logout/', views.logout_view, name='logout'),
]

