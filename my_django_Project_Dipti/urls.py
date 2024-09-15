from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', include('crud.urls')),
    path('auth/',include('auth_app.urls'))
]
