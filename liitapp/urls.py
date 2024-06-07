from django.urls import path
from .import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('completeRegister/<str:register_id>',views.completeRegister,name='completeRegister'),
    path('viewRegistrations',views.viewRegistrations,name='viewRegistrations'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)