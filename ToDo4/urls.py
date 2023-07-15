from django.urls import path

from django.contrib import admin
from django.urls import path, include
from users import views
# to make possible include images in templates
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

