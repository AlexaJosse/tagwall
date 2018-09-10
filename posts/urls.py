from django.urls import path, re_path

from . import views
app_name="posts"

urlpatterns = [
    path('postdetails/<int:post_id>', views.postdetails, name='postdetails'),
    path('newpost/', views.newpost, name='newpost'),
    path('P<int:post_id>/upvote/', views.upvote, name='upvote'),
    path('P<int:post_id>/downvote/', views.downvote, name='downvote'),
    path('P<int:post_id>newtag/',views.newtag,name="newtag"),

]
