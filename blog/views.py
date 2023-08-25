# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import generics, permissions
# from .models import Blog, TagBlog, SubContent, Comment
# from .serializers import TagBlogSerializer, BlogSerializer, BlogPostSerializer, SubContentSerializer, \
#     CommentUserIsAuthenticatedSerializer, CommentUserIsNotAuthenticatedSerializer, \
#     CommentUserIsAuthenticatedPostSerializer, CommentUserIsNotAuthenticatedPostSerializer
# from main.views import AllPagination
#
#
# # TAG
# class TagBlogListCreteAPIView(generics.ListCreateAPIView):
#     # http://127.0.0.1:8000/blog/tag/
#     queryset = TagBlog.objects.all()
#     serializer_class = TagBlogSerializer
#     pagination_class = AllPagination
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title']
#
#
# class TagBlogRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
#     # http://127.0.0.1:8000/blog/tag/{tag_id}/
#     queryset = TagBlog.objects.all()
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     serializer_class = TagBlogSerializer
#
#
# class BlogListCreateAPIView(generics.ListCreateAPIView):
#     # http://127.0.0.1:8000/blog/blog/
#     queryset = Blog.objects.order_by('-id')
#     pagination_class = AllPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title', 'description', 'tags']
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return BlogPostSerializer
#         return BlogSerializer
#
#
# class BlogRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
#     # http://127.0.0.1:8000/blog/blog/{blog_id}/
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# # SUB-CONTENT
# class SubContentListCreateAPIView(generics.ListCreateAPIView):
#     # http://127.0.0.1:8000/blog/sub-content/
#     queryset = SubContent.objects.order_by('-id')
#     serializer_class = SubContentSerializer
#     pagination_class = AllPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title', 'description']
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# class SubContentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
#     # http://127.0.0.1:8000/blog/sub-content/{sub-content_id}/
#     queryset = SubContent.objects.all()
#     serializer_class = SubContentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# # COMMENT
# class CommentListCreateAPIView(generics.ListCreateAPIView):
#     # http://127.0.0.1:8000/blog/blog/{blog_id}/comment/
#     queryset = Comment.objects.order_by('-id')
#     pagination_class = AllPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title', 'name', 'email', 'website', 'blog', 'body', 'created_date']
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             if self.request.user.is_authenticated:
#                 return CommentUserIsAuthenticatedSerializer
#             return CommentUserIsNotAuthenticatedSerializer
#         else:
#             if self.request.user.is_authenticated:
#                 return CommentUserIsAuthenticatedPostSerializer
#             return CommentUserIsNotAuthenticatedPostSerializer
#
#     # def get_serializer_context(self):
#     #     ctx = super().get_serializer_context()
#     #     ctx['blog_id'] = self.kwargs.get('blog_id')
#     #     return ctx
#     #
#     # def get_queryset(self):
#     #     qs = super().get_queryset()
#     #     blog_id = self.kwargs.get('blog_id')
#     #     qs = qs.filter(blog_id=blog_id)
#     #     return qs
