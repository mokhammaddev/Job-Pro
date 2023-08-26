from django.urls import path
from . import views

urlpatterns = [
    # JOBS
    path('jobs/', views.JobsListCreateAPIView.as_view()),
    path('jobs/<int:pk>/', views.JobsRUDAPIView.as_view()),
    # CATEGORY
    path('category/', views.CategoryListCreateAPIView.as_view()),
    path('catgeory/<int:pk>/', views.CategoryRUDAPIView.as_view()),
    # TAG
    path('tag/', views.TagListCreateAPIView.as_view()),
    path('tag/<int:pk>/', views.TagRUDAPIView.as_view()),
    # SELECTION-LIST
    path('selection-list/', views.SelectionListListCreateAPIView.as_view()),
    path('selection-list/<int:pk>/', views.SelectionListRUDAPIView.as_view()),
]
