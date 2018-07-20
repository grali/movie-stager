from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	  path("auth/",include("authentication.urls")),
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls', namespace='movies')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
