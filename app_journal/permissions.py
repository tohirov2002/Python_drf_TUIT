from rest_framework.permissions import BasePermission


class IsAdminReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.method == 'GET'


# class IsAuthorReadOnly(BasePermission):
#
#     def has_permission(self, request, view):
#         if request.method == 'GET':
#             return True
#         elif request.user.is_staff and request.method == 'POST':
#             return True
#         return view.get_object().author == request.user
