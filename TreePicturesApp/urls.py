from django.urls import path
from .views import TreePictureFormView, TreePictureDetail, TreePictureList
from TreePictures import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "pictures"
urlpatterns = [
    path('', TreePictureFormView.as_view(), name='picture_form'),
    path('detail/<int:pk>/', TreePictureDetail.as_view(), name='detail'),
    path('list/', TreePictureList.as_view(), name='picture_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)