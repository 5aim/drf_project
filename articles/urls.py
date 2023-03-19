from django.urls import path
from articles import views


urlpatterns = [
    path("", views.ArticleAV.as_view(), name="article_view"),
    path("<int:article_id>/", views.ArticleDV.as_view(), name="article_detail_view"),
    path("comment/", views.CommentAV.as_view(), name="comment_view"),
    path("comment/<int:comment_id>", views.CommentDV.as_view(), name="comment_detail_view"),
    path("thumbs/", views.ThumbsAV.as_view(), name="thumbs_view"),
]
