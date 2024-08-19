'''
message_board app urls
'''
from django.urls import path
from . import views


urlpatterns = [
    path('board/', views.MessageBoard.as_view(), name="message_board"),
    path('board/post', views.new_post, name="new_post"),
    path('board/<slug:slug>/reply', views.new_reply, name="new_reply"),
    path('board/post/edit/<slug:slug>', views.edit_post, name="edit_post"),
    path('board/<slug:slug>', views.view_post, name="view_post"),
    path('board/delete_post/<slug:slug>',
         views.delete_post, name="delete_post"),
    path('board/edit_reply/<slug:slug>/<int:comment_id>',
         views.edit_reply, name="edit_reply"),
    path('board/delete_reply/<slug:slug>/<int:reply_id>',
         views.delete_reply, name="delete_reply"),
]
