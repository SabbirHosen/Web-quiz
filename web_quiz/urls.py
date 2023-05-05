"""web_quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from quiz import views as quiz_views
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Quiz Maker"
admin.site.site_title = "Quiz Maker Administration"
admin.site.index_title = "Quiz Maker Admin panel"

handler404 = "quiz.views.error_404"
handler500 = "quiz.views.error_500"

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^', include('quiz.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

