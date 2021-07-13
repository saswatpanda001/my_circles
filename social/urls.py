from django.urls import path
from social import views


app_name = "social"


urlpatterns = [
    path("post", views.post_view, name="wall"),
    path("postform", views.postform_view.as_view(), name="create"),
    path("profile/<int:pk>", views.mypost_view, name="profile"),
    path("messages", views.msglist_view, name="msglist"),
    path("profile/<int:pk>/text", views.text_view, name="text"),
    path("profile/<int:pk>/text/send", views.send_view, name="send"),
    path("profile/<int:pk>/text/get_mes", views.get_mes, name="get_mes"),
    
    path("post/<int:pk>", views.postdetail_view, name="post_detail"),
    path("post/<int:pk>/update", views.post_editview.as_view(), name="update"),
    path("post/<int:pk>/delete", views.post_deleteview.as_view(), name="delete"),
    path("my_post/update/<int:pk>", views.profile_updateview.as_view(),
         name="profile_update"),

    path('chat/', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),


    path("feedback", views.feedback_view.as_view(), name="feedback"),
    path("greetings", views.greetings_view, name="greetings"),
    # path('user_search', views.usersearch_view.as_view(), name="user_search"),

]
