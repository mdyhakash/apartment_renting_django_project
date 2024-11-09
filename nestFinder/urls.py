from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static
from accounts import views as acc_views # type: ignore
from property import views as prop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', prop_views.home, name="home"),
    path('login/', acc_views.login, name='login'),
    path('signup/', acc_views.signup, name='signup'),
    path('apartment/', prop_views.apartment, name='apartment'),
    path('propertydetails/<str:p_id>',prop_views.propertydetails,name='propertydetails')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
