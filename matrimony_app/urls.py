from django.urls import path
from matrimony_app import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('update_profile', views.update_profile, name="update_profile" ),
    path('logins', views.logins, name="logins" ),
    path('logouts', views.logouts, name="logouts" ),
    path('my_profile', views.my_profile, name="my_profile" ),
    path('all_profiles', views.all_profiles, name="all_profiles" ),
    path('regs', views.regs, name="regs" ),
    path('view_profile/<ID>', views.view_profile, name="view_profile" ),
]
