"""mars_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
import orders_app.views

# Comment
# Another comment to peter branch
# One more comment to peter branch
# Last comment to peter branch

urlpatterns = [
                  path('orders_app/', include('orders_app.urls')),
                  path('admin/', admin.site.urls),
                  path('', orders_app.views.mainpage, name='mainpage'),
                  path('devices/', orders_app.views.get_devices, name='get_devices'),
                  path('devpage/', orders_app.views.devpage, name='devpage')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
