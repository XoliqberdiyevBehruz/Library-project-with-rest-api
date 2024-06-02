from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status


# class ListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class ListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "success": f"Returned {len(books)} books",
            "books": serializer_data,
        }

        return Response(data)


# class DetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = "id"

class DetailApiView(APIView):

    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Exception:
            data = {
                "status": "Book doesn't exists",
                "message": "Book didn't find",
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)


# class UpdatelApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = "id"

class UpdatelApiView(APIView):

    def put(self, request, id):
        book = get_object_or_404(Book.objects.all(), id=id)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        data = {
            "success": True,
            "message": f"Book {book_saved} is successfully updated.",
        }
        return Response(data)



# class DeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = "id"

class DeleteApiView(APIView):

    def delete(self, request, id):
        try:
            book = Book.objects.get(id=id)
            book.delete()
            data = {
                "status":True,
                "message": "Book successfully deleted",
            }
            return Response(data, status=status.HTTP_200_OK)

        except Exception:
            data = {
                "status": False,
                "message": "Book is not found",
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

# class CreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class CreateApiView(APIView):

    def post(self, request):
        book = request.data
        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                "success": True,
                "message": "Book is created successfully",
                "created book": book,
            }
            return Response(data)
        else:
            data = {
                "success": False,
                "message": "Book isn't created what's the wrong, please tyr again."
            }
            return Response(data)

class ListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RetrieveDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"


class RetrieveDestroyUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer