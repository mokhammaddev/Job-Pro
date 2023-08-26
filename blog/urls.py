from django.urls import path
from .views import BlogListCreateAPIView, TagBlogListCreteAPIView, TagBlogRUDAPIView, BlogRUDAPIView, \
    SubContentListCreateAPIView, SubContentRUDAPIView, CommentListCreateAPIView

urlpatterns = [
    # TAG
    path('tag/', TagBlogListCreteAPIView.as_view()),
    path('tag/<int:pk>/', TagBlogRUDAPIView.as_view()),
    # BLOG
    path('blog/', BlogListCreateAPIView.as_view()),
    path('blog/<int:pk>/', BlogRUDAPIView.as_view()),
    # SUB-CONTENT
    path('sub-content/', SubContentListCreateAPIView.as_view()),
    path('sub-content/<int:pk>/', SubContentRUDAPIView.as_view()),
    # COMMENT
    path('blog/<int:pk>/comment/', CommentListCreateAPIView.as_view()),
]
