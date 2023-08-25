# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import generics, permissions
# from .models import Jobs, TagJobs, CategoryJobs, SelectionList
# from .serializers import JobsSerializer, JobsPostSerializer, TagJobsSerializer, CategoryJobsSerializer,\
#     SelectionListSerializer
# from main.views import AllPagination
#
#
# # JOBS
# class JobsListCreateAPIView(generics.ListCreateAPIView):
#     # http://127.0.0.1:8000/jobs/jobs/
#     queryset = Jobs.objects.order_by('-id')
#     # permission_classes = (IsOwnHR, )
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     pagination_class = AllPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['author', 'title', 'company', 'category', 'price']
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return JobsPostSerializer
#         return JobsSerializer
#
#
# class JobsRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
#     # http://127.0.0.1:8000/jobs/jobs/{jobs_id}/
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Jobs.objects.all()
#     serializer_class = JobsSerializer
#
#
# # CATEGORY
# class CategoryListCreateAPIView(generics.ListCreateAPIView):
#     # http://127.0.0.1:8000/jobs/category/
#     queryset = CategoryJobs.objects.all()
#     serializer_class = CategoryJobsSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     pagination_class = AllPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title']
#
#
# class CategoryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
#     # http://127.0.0.1:8000/jobs/category/{category_id}/
#     queryset = CategoryJobs.objects.all()
#     serializer_class = CategoryJobsSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# # TAG
# class TagListCreateAPIView(generics.ListCreateAPIView):
#     # http://127.0.0.1:8000/jobs/tag/
#     queryset = TagJobs.objects.all()
#     serializer_class = TagJobsSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     pagination_class = AllPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title']
#
#
# class TagRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
#     # http://127.0.0.1:8000/jobs/tag/{tag_id}/
#     queryset = TagJobs.objects.all()
#     serializer_class = TagJobsSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# # SELECTION LIST
# class SelectionListListCreateAPIView(generics.ListCreateAPIView):
#     # http://127.0.0.1:8000/jobs/selection-list/
#     queryset = SelectionList.objects.order_by('-id')
#     serializer_class = SelectionListSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['author', 'jobs']
#
#     def get_serializer_context(self):
#         ctx = super().get_serializer_context()
#         ctx['author_id'] = self.kwargs.get('author_id')
#         return ctx
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         author_id = self.request.user.id
#         qs = qs.filter(author_id=author_id)
#         return qs
#
#
# class SelectionListRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
#     # http://127.0.0.1:8000/jobs/selection-list/{selection-list_id}/
#     queryset = SelectionList.objects.all()
#     serializer_class = SelectionListSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
