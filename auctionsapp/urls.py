from django.urls import path
# from .views import UserDeleteAPIView
from . import views 
urlpatterns = [


    path('', views.hellow),
    path('delete/<int:pk>', views.aucdel),

    path('edit/<int:pk>', views.aucedit),
    path('test2', views.TESTView),


    
    
]
# from django.conf import settings  
# from django.conf.urls.static import static  
# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  