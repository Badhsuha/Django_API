from django.shortcuts import render
import jwt
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import AdvisorSerielizer, RegisterUserSerielizer,BookingSerializer
from .models import User, Advisor,Booking

SECRET_KEY = 'anykey'


class AdvisorView(APIView):
    def post(self, request, *args, **kwargs):
        serialized_data = AdvisorSerielizer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response("200_OK", 200)
        return Response("400_BAD_REQUEST", 400)


class RegisterUser(APIView):
    def post(self, request, *args, **kwargs):
        serialized_data = RegisterUserSerielizer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            qs = User.objects.get(email=serialized_data.data['email'])
            id = qs.id
            token = jwt.encode({"name": serialized_data.data['name'], "email": serialized_data.data['email'] }, SECRET_KEY , algorithm="HS256")
            return Response({'id':id, 'token':token})
        return Response("400_BAD_REQUEST", 400)


class LoginUser(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        if not data.get('email') or not data.get('password'):
            return Response('400_BAD_REQUEST', 400)
        try:
            qs = User.objects.get(email=data['email'])
            if qs.password.strip() != data['password'].strip():
                return Response('401_AUTHENTICATION_ERROR' , 401)
        except:
            return Response('401_AUTHENTICATION_ERROR' ,401)

        token = jwt.encode({"name": qs.id, "email": qs.email }, SECRET_KEY , algorithm="HS256")
        return Response({'user-id':qs.id, 'token':token}, 200)


class GetAdvisor(APIView):
    def get(self, *args, **kwargs):
        try:
            User.objects.get(id=kwargs['id'])
        except:
            return Response(401)
        qs = Advisor.objects.all()
        serialized_data = AdvisorSerielizer(qs, many=True)
        return Response(serialized_data.data, 200)


class BookAdvisor(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=kwargs['user_id'])
            advisor = Advisor.objects.get(id=kwargs['adv_id'])
            serialized_data = BookingSerializer(data={'dateTime':request.data['dateTime'], 'adv_id':advisor.pk, 'user_id': user.pk})
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(200)
            return Response(401)
        except:
            return Response(401)

    def get(self, *args, **kwargs):
        try:
            booking = Booking.objects.all().filter(user_id=kwargs['user_id'])
            data = [{'advisor_Name': bk.adv_id.name,'advisor_Prof_Pic':bk.adv_id.photo_url,
                      'advisor_id': bk.adv_id.id , 'booking_id': bk.id,  'booking_time': bk.dateTime} for bk in booking]

            return Response(data, 200)
        except:
            return Response(401)
