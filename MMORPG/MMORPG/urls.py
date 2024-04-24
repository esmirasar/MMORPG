from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('test/', TemplateView.as_view(template_name='default.html')),
    path('registration/', include('registration.urls')),
    path('response/', include('response.urls'))
]
urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)