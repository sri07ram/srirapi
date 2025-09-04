from django.urls import path
from .views import CreateMailView,GetAllMailView,UpdateMailView,DeleteMailView

urlpatterns=[
    path('mails/',CreateMailView.as_view(),name='create-mails'),
    path('mails/all/',GetAllMailView.as_view(),name='get-mail'),
    path('mails/<int:pk>/update/',UpdateMailView.as_view(),name='update-mail'),
    path('mails/<int:pk>/delete/',DeleteMailView.as_view(),name='delete-mail'),
]