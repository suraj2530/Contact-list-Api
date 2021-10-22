from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions


class ContactList(ListCreateAPIView):

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # lookup_field = "id"

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

        # this querset work as since we only need our objects unlike in review where we need 
        # multiple people review and can edit only our own so permission class IsOwnerOrReadOnly n



