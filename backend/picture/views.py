from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .serializers import PictureSerializer
from .models import Picture
from .service import *
import base64
from io import BytesIO
class PictureMixinView(
    generics.GenericAPIView, 
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    ):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    lookup_field = "picture_id"

    def get(self, request, *args, **kwargs):
        picture_id = kwargs.get('picture_id')
        if picture_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(*args, **kwargs)
        try:
            file_name = request.data['file_name']
            file_name_parts = parts_file_name(file_name)
            status = get_status(file_name_parts)
            request.data['status'] = status
            if status:
                cap_time = get_cap_time(file_name_parts)
                request.data['cap_time'] = cap_time
            inf_result, inf_conf = get_inf_data(file_name_parts)
            request.data['inf_result'], request.data['inf_conf'] = inf_result, inf_conf
            inference_ms = get_inference_ms(file_name_parts)
            print(type(inference_ms))
            request.data['inference_ms'] = inference_ms
            file_path = f'picture/image/{file_name}'
            file_data = request.data['file_data']
            save_base64_image(file_data, file_path)
            '''
            Real situation !!!!
            - Extract the base64 string from request.data
            - Use the file_name to generate a file path
            - use base64 string and file path to write an image file
            - then use that path in getting the link
            - for testing purpose, without having to use a long ass base64 string
                import the image into this project, use the base64 converter to convert
                the image to base64 string, store it in a variable.
                -> set the file_data as the variable, pass it into the serializer
                -> During the post method, use base64 string to create a local image
                -> use the image path in creating media file
            - note that this serializer does not take account of posting the same image
                because that will be likely to never happen
            '''
            # base_64_string = request.data.get('file_data')
            # file_name = request.data.get('file_name')
            robot_id = request.data.get('robot_id')
            print('robot id:', robot_id)
            # base_64_bytes = base_64_string.encode('utf-8')
            # image_data = base64.b64decode(base_64_bytes)
            # file_data = BytesIO(image_data)
            # file_data.seek(0)

            drive_link = get_drive_link(file_path, file_name, robot_id)
            print('Drive Link:' ,drive_link)
            request.data['url'] = drive_link
            return self.create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({"errors": e.detail})
        except KeyError as e:
            return Response({"errors": f"Missing required field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        return serializer.save()
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)