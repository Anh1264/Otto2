from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .serializers import ActivitySerializer
from rest_framework import generics, mixins
from .models import Activity
from robot.models import Robot
from .service import get_datetime_object
from rest_framework.response import Response

# Create your views here.

# class ActivityListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer

# class ActivityDetailAPIView(generics.RetrieveAPIView):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer
#     lookup_field = 'pk'

# class ActivityUpdateAPIView(generics.UpdateAPIView):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer
#     lookup_field = 'pk'

# class ActivityDestroyAPIView(generics.DestroyAPIView):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer
#     lookup_field = 'pk'


class ActivityCreateAPIView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    def perform_create(self, serializer):
        # extra_data = {'hello': 'world'}
        # serializer.save(**extra_data)
        serializer.save()

    def post(self, request, *args, **kwargs):
        print("request data:", request.data)
        request.data['on_time'], request.data['off_time'], request.data['active_time'] = get_datetime_object(request.data['off_time'], request.data['session_seconds'])
        print(request.data['on_time'], request.data['off_time'], request.data['active_time'])
        print(request.data)
        serialize = self.get_serializer(data = request.data)
        if not serialize.is_valid():
            print("Validation error:", serialize.errors)
            return Response(serialize.erros)
        return self.create(request, *args, **kwargs) #validate serialzer then call perform create
    
class ActivityReadAPIView(
    generics.GenericAPIView, 
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    ):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
class RobotActivitiesReadAPIView(
generics.GenericAPIView, 
mixins.ListModelMixin,
mixins.RetrieveModelMixin,
):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        robot_id = self.kwargs.get('robot_id')
        queryset = Activity.objects.filter(robot_id=robot_id)
        return queryset
    
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        robot_id = kwargs.get('robot_id')
        if robot_id is not None:
            return self.list(request, *args, **kwargs)
        return Response({'detail': 'Robot id is required!'}, status=400)


class ActivityUpdateAPIView(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    

class ActivtyDestroyAPIView(
    generics.GenericAPIView,
    mixins.DestroyModelMixin,
):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    lookup_field = 'pk'

    def delete(self, request , *args, **kwargs):
        return self.destroy(request, *args, **kwargs)