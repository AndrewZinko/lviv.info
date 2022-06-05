from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('recommended', views.recommended, name="recommended"),
    path('recommended/<int:pk>', views.ArticleDetailView.as_view(), name="article"),
    path('about-us', views.about_us, name="about-us"),
    path('about-me', views.about_me, name="about-me")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
