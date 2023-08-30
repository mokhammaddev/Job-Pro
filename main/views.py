from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from .models import Company, Type, City, Country, Contact, Position, Subscribe
from .serializers import CountrySerializer, ContactSerializer, CityPostSerializer, \
    TypeSerializer, CityGetSerializer, PositionSerializer, CompanySerializer, SubscribeSerializer


class AllPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'


# CONTACT
class ContactListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/main/category/
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = AllPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email', 'subject', 'message']


class ContactRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/main/position/{contact_id}/
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# TYPE
class TypeListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/main/type/
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    pagination_class = AllPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']


class TypeRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/main/position/{type_id}/
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# COUNTRY
class CountryListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/main/country/
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = AllPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']


class CountryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/main/position/{country_id}/
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# CITY
class CityListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/main/city/
    queryset = City.objects.all()
    pagination_class = AllPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'country']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CityPostSerializer
        return CityGetSerializer


class CityRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/main/position/{city_id}/
    queryset = City.objects.all()
    serializer_class = CityPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# POSITION
class PositionListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/main/position/
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    pagination_class = AllPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']


class PositionRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/main/position/{position_id}/
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# COMPANY
class CompanyListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/main/company/
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = AllPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'location']


class CompanyRUDAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/main/company/{company_id}/
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# SUBSCRIBE
class SubscribeListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/main/subscribe/
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    pagination_class = AllPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email']


class SubscribeRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/main/subscribe/{subscribe_id}/
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
