"""projproducts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import debug

admin.site.site_title = admin.site.site_header = settings.APPN_ADMIN_NAME
admin.site.site_url = settings.APPN_ADMIN_HOST

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', debug.default_urlconf),

    # -> API's
    path('products/', include('products.urls')),
    path('home/', include('home.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)