from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('manager/', admin.site.urls),
    path('admin-panel/', include('admin_panel.urls'))
]
