from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    path('emp', views.emp,name='emp'),  
    path('show',views.show,name='show'),  
    path('edit/<int:id>', views.edit,name='edit'),  
    path('update/<int:id>', views.update,name='update'),  
    path('delete/<int:id>', views.destroy,name='destroy'),  
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)