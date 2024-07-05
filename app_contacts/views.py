from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.mail import send_mail

from .models import ContactsModel
from conf.settings import EMAIL_HOST_USER
from .serializers import ContactsSerializer


class SendContactsView(viewsets.ModelViewSet):
    queryset = ContactsModel.objects.all()
    serializer_class = ContactsSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        first_name = request.data.get("first_name")
        email = request.data.get("email")
        message = request.data.get("message")
        try:
            send_mail(
                subject=first_name,
                message=f"{message} \n" f" {email}",
                from_email=EMAIL_HOST_USER,
                recipient_list=["tohirovahmad07@gmail.com"],
                fail_silently=False,
            )
            return Response(
                {"success": "Email sent successfully"}, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
