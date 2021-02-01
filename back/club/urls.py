from django.urls import path
from . import views 

urlpatterns = [
    path('',views.club_list),
    path('create/',views.club_create),
    path('club_detail/<str:club_pk>/',views.club_detail),
    path('club_article/',views.club_article),
    path('club_article_detail/<str:club_article_pk>/',views.club_article_detail),
    path('club_signup/<str:club_pk>/',views.club_signup),
    path('club_member_delete/<str:club_pk>/',views.club_member_delete),
]