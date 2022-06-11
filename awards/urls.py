from django.urls import path
from . import views
from .views import *
from . import views as app_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # PROFILE SECTION
    path('profile/', profile, name='users-profile'),
    path('profile/update/',app_views.update_profile,name='update_profile'),
    path('new/profile$', views.add_profile, name='new_profile'),

    # MAIN PAGE 
    path('', views.index, name='index'),

    # POST SECTION

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)