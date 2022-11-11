from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Draw
from .serializers import DrawSerializer

class DrawListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the drawings items
        '''
        draws = Draw.objects.all()
        serializer = DrawSerializer(draws, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the draw with given drawing data
        '''
        data = {
            'draw_title': request.data.get('draw_title'), 
            'draw_payload': request.data.get('draw_payload')
        }
        serializer = DrawSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DrawDetailApiView(APIView):

    def get_object(self, draw_id):
        '''
        Helper method to get the object with given draw_id
        '''
        try:
            return Draw.objects.get(id=draw_id)
        except Draw.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, draw_id, *args, **kwargs):
        '''
        Retrieves the Todo with given draw_id
        '''
        draw_instance = self.get_object(draw_id)
        if not draw_instance:
            return Response(
                {"res": "Object with draw id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = DrawSerializer(draw_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, draw_id, *args, **kwargs):
        '''
        Updates the draw item with given draw_id if exists
        '''
        draw_instance = self.get_object(draw_id)
        if not draw_instance:
            return Response(
                {"res": "Object with draw id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'draw_title': request.data.get('draw_title'), 
            'draw_payload': request.data.get('draw_payload'),
        }
        serializer = DrawSerializer(instance = draw_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, draw_id, *args, **kwargs):
        '''
        Deletes the draw item with given draw_id if exists
        '''
        draw_instance = self.get_object(draw_id)
        if not draw_instance:
            return Response(
                {"res": "Object with draw id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        draw_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )



