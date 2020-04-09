from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
import logging

from .models import  #Models
from .serializers import *

logger = logging.getLogger(__name__) 

# Create your views here.

class CustomAuthToken(ObtainAuthToken):

    """https://www.django-rest-framework.org/api-guide/authentication/"""

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            logger.info(f'{user.name} ({user.pk}) logged in.')
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'name': user.name
            })
        except:
            logger.error(f'CustomAuthToken failed - request not authorized')
            return Response({
                'token': False
            })

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def ex(request):
    try:
        data = Models.objects.all().exclude(id=x)
    except:
        logger.error(f'Request failed with token: {request.auth} - func ex')
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = Serializer(data=data, context={'request': request}, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_202_ACCEPTE)
