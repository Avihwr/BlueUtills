from django.urls import path
from ImageUtils import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('imageutils/', views.photo_list, name='photo_list'),
    path('imageutils/delete/', views.delete, name='delete'),

]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
