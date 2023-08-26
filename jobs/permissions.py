from rest_framework import permissions
from rest_framework.response import Response
from .models import Jobs

# class IsOwnUserReadonly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.id == request.user.id
#


class IsOwnHR(permissions.BasePermission):

    def has_permission(self, request, view):
        print(3333333, request.user.role)
        if request.user.role == 0:
            instance = Jobs.objects.create()
            return instance
        return Response("You are not Resource Management")







