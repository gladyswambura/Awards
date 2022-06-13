from django.urls import path, include
from . import views
from .views import *
from . import views as app_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
# from registration.backends.simple.views import RegistrationView
# from awards.forms import RegisterForm


urlpatterns = [
    #AUTHENTICATION
    # path('accounts/register/', RegistrationView.as_view(form_class=RegisterForm),name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('logout/', auth_views.logout_then_login),

    # MAIN PAGE                                      
    path('', views.index, name='index'),

    # PROFILE SECTION
    path('profile/', views.profile, name='users-profile'),
    

    #SITE SECTION
    path('site/<id>', views.site_detail, name='site_results'),
    path('new/site', views.new_site, name='new-site'),

    # RATING SECTION
    path('ratings/', include('star_ratings.urls', namespace='ratings')),

    # SEARCH SECTION
    path('search/', views.search, name='search'),

    # API SECTION
    path('api/site/', views.SitesList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)