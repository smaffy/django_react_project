from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login_view, name='api-login'),         # allows the user to log in by providing their username and password
    path('logout/', views.logout_view, name='api-logout'),      # logs the user out
    path('session/', views.session_view, name='api-session'),   # checks whether a session exists
    path('whoami/', views.whoami_view, name='api-whoami'),      # fetches user data for an authenticated user

]
