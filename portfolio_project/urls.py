from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from portfolio.admin import portfolio_admin_site


urlpatterns = [
    path("admin/", portfolio_admin_site.urls),
    path("", include("portfolio.urls")),
]

# During development, Django can serve uploaded images for us.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
