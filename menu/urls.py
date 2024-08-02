from django.urls import path 
from . import views 
from django.conf.urls.static import static  # new
from django.conf import settings  # new

urlpatterns = [
    path('',views.menu,name='menu'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new

