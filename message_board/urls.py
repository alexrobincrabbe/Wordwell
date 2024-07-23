from . import views
from django.urls import path

urlpatterns = [
    path('board/', views.MessageBoard.as_view(), name="message_board"),
    path('board/post', views.new_post, name="new_post"),
    path('board/<slug:slug>', views.view_post, name="view_post"),
]