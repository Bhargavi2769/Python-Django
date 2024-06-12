from django.urls import path
from .views import ConversationList
from .views import FileUploadView

from .views import FileListView

from .views import FileDeleteView




urlpatterns = [
    path('conversations/', ConversationList.as_view(), name='conversation-list'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('files/', FileListView.as_view(), name='file-list'),
    path('files/<int:pk>/', FileDeleteView.as_view(), name='file-delete'),
]



