from django.shortcuts import render
from .models import TrackAndTrace
from rest_framework import generics
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import TrackAndTraceSerializer


# class TrackAndTraceCreate(generics.CreateAPIView):
#     queryset = (TrackAndTrace.objects.all(),)
#     serializer_class = TrackAndTraceSerializer


class TrackAndTraceCreate(generics.CreateAPIView):
    serializer_class = TrackAndTraceSerializer
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            messages = []
            for message_data in request.data:
                serializer = self.get_serializer(data=message_data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                messages.append(serializer.data)
            return Response(messages, status=status.HTTP_201_CREATED)
        else:
            return super().create(request, *args, **kwargs)

class TrackAndTraceList(generics.ListAPIView):
    # API endpoint that allows TrackAndTrace to be viewed.
    queryset = TrackAndTrace.objects.all()
    serializer_class = TrackAndTraceSerializer


class TrackAndTraceDetailList(generics.ListAPIView):
    serializer_class = TrackAndTraceSerializer
    lookup_field = 'device_id'
    def get_queryset(self):
        queryset = TrackAndTrace.objects.all()
        queryset = queryset.order_by('-id')
        valid_field_names = [field.name for field in TrackAndTrace._meta.get_fields()]
        # Loop through all URL parameters and filter the queryset
        for param, value in self.request.query_params.items():
            if param != 'limit' and param in valid_field_names:
                queryset = queryset.filter(**{param: value})
        limit = int(self.request.query_params.get('limit', 20)) #default to 20
        total_objects = queryset.count()
        if limit > total_objects:
            limit = total_objects
        return queryset[:limit]


class TrackAndTraceUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a TrackAndTrace record to be updated.
    queryset = TrackAndTrace.objects.all()
    serializer_class = TrackAndTraceSerializer

class TrackAndTraceDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a TrackAndTrace record to be deleted.
    queryset = TrackAndTrace.objects.all()
    serializer_class = TrackAndTraceSerializer
