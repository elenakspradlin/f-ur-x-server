from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from furxapi.models import UserProfileInformation


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=username, password=password)

    # If authentication was successful, respond with their token
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)

        data = {
            'valid': True,
            'token': token.key,
            # 'staff': authenticated_user.is_staff
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data.get('username', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    password = request.data.get('password', None)

    if username is not None \
            and first_name is not None \
            and last_name is not None \
            and password is not None:

        try:
            new_user = User.objects.create_user(
                username=request.data['username'],
                password=request.data['password'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name']
            )

            user_profile = UserProfileInformation.objects.create(
                user=new_user,
                bio=request.data['bio'],
                day_of_breakup=request.data['day_of_breakup'],
            )

        except IntegrityError:
            return Response(
                {'message': 'An account with that username already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # account = None

        # if account_type == 'customer':
        # account = Customer.objects.create(
        # address=request.data['address'],
        # user=new_user
        # )
        # elif account_type == 'employee':
        # new_user.is_staff = True
        # new_user.save()

        # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=user_profile.user)
        # Return the token to the client
        data = {'token': token.key}
        return Response(data)

    return Response({'message': 'You must provide username, password, first_name, and last_name'}, status=status.HTTP_400_BAD_REQUEST)
