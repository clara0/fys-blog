# blog/urls.py

from django.urls import path
from . import views
from fys_blog import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
