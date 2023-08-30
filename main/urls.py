from django.urls import path
from .views import TypeListCreateAPIView, TypeRUDAPIView, CityListCreateAPIView, CityRUDAPIView, \
    CountryListCreateAPIView, CountryRUDAPIView, ContactListCreateAPIView, ContactRUDAPIView, \
    PositionListCreateAPIView, PositionRUDAPIView, CompanyListCreateAPIView, CompanyRUDAPIView,\
    SubscribeListCreateAPIView, SubscribeRUDAPIView

urlpatterns = [
    # CONTACT
    path('contact/', ContactListCreateAPIView.as_view()),
    path('contact/<int:pk>/', ContactRUDAPIView.as_view()),
    # TYPE
    path('type/', TypeListCreateAPIView.as_view()),
    path('type/<int:pk>/', TypeRUDAPIView.as_view()),
    # COUNTRY
    path('country/', CountryListCreateAPIView.as_view()),
    path('country/<int:pk>/', CountryRUDAPIView.as_view()),
    # CITY
    path('city/', CityListCreateAPIView.as_view()),
    path('city/<int:pk>/', CityRUDAPIView.as_view()),
    # POSITION
    path('position/', PositionListCreateAPIView.as_view()),
    path('position/<int:pk>/', PositionRUDAPIView.as_view()),
    # COMPANY
    path('company/', CompanyListCreateAPIView.as_view()),
    path('company/<int:pk>/', CompanyRUDAPIView.as_view()),
    # SUBSCRIBE
    path('subscribe/', SubscribeListCreateAPIView.as_view()),
    path('subscribe/<int:pk>/', SubscribeRUDAPIView.as_view()),
]
