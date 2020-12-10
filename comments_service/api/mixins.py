from rest_framework.response import Response
from rest_framework import status


class ActionFavoriteMixin:

    def action_with_favorite(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       