from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.user.role == 'manager':
            return True

        return obj.author == request.user



#comment permissions
class IsCommentAuthorOrManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.user.role == "manager":
            return True

        return obj.author == request.user
