from django.core.mail import send_mail
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Library, Book, Author
from .api.serializers.serializer import LibrarySerializer, BookSerializer
from .api.serializers.serializer import AuthorSerializer, LeadsSerializer


@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def library_abm_view(request, pk_library=None):
    '''
    Crea la vista Libreria (ABM) que contiene
    Modelo : Library
    Path: domain/api/library/{id}
    Acciones Permitidas: GET | POST | PUT
    Formato de respuest: JSON
    '''
    if request.method == 'GET':
        library = Library.objects.filter(id=pk_library).first()
        library_serializer = LibrarySerializer(library)
        return Response(
            library_serializer.data,
            status=status.HTTP_200_OK
        )
    elif request.method == 'POST':
        library_serializer = LibrarySerializer(data=request.data)
        if library_serializer.is_valid():
            library_serializer.save()
            return Response(
                library_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                library_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    elif request.method == 'PUT':
        library = Library.objects.get(id=pk_library)
        library_serializer = LibrarySerializer(library, data=request.data)
        if library_serializer.is_valid():
            library_serializer.save()
            return Response(
                library_serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                library_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def library_filter_view(request, pk_book=None):
    '''
    Crea la vista Libros Filtor que contiene
    Modelo : Library
    Path: domain/api/library/{id}/books/{id}
    Acciones Permitidas: GET
    Formato de respuest: JSON
    '''
    if pk_book:
        if request.method == 'GET':
            book = Book.objects.filter(libraries__id=pk_book)
            book_serializer = BookSerializer(book, many=True)
            return Response(book_serializer.data)


@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def libros_abm_view(request, pk=None):
    '''
    Crea la vista Libros (ABM) que contiene
    Modelo : Book
    Path: domain/api/book/{id}
    Acciones Permitidas: GET | POST | PUT
    Formato de respuest: JSON
    '''
    if request.method == 'GET':
        book = Book.objects.filter(id=pk).first()
        book_serializer = BookSerializer(book)
        return Response(
            book_serializer.data,
            status=status.HTTP_200_OK
        )
    elif request.method == 'POST':
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(
                book_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                book_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    elif request.method == 'PUT':
        book = Book.objects.get(id=pk)
        book_serializer = BookSerializer(book, data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(
                book_serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                book_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def libro_buscar_view(request):
    '''
    Libros (Búsqueda)
    Modelo : Book
    Path: domain/api/book/search?text=”título de libro”
    Acciones Permitidas: GET
    Formato de respuest: JSON
    '''

    if request.method == 'GET':
        criterio = request.GET.get('text')
        book = Book.objects.filter(title=criterio).first()
        book_serializer = BookSerializer(book)
        return Response(
            book_serializer.data,
            status=status.HTTP_200_OK
        )


@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def autores_abm_view(request, pk=None):
    '''
    Crea la vista Autores (ABM) que contiene
    Modelo : Book
    Path: domain/api/author/{id_book}
    Acciones Permitidas: GET | POST | PUT
    Formato de respuest: JSON

    '''
    if request.method == 'GET':
        author = Author.objects.filter(book__id=pk).get()

        author_serializer = AuthorSerializer(author)
        return Response(
            author_serializer.data,
            status=status.HTTP_200_OK
        )
    elif request.method == 'POST':
        author_serializer = AuthorSerializer(data=request.data)
        if author_serializer.is_valid():
            author_serializer.save()
            return Response(
                author_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                author_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    elif request.method == 'PUT':
        author = Author.objects.filter(book__id=pk).get()
        author_serializer = AuthorSerializer(author, data=request.data)
        if author_serializer.is_valid():
            author_serializer.save()
            return Response(
                author_serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                author_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def leads_create_view(request):
    '''
    Crea la vista Leads Crear que contiene
    Modelo : Lead
    Path: domain/api/lead
    Acciones Permitidas: POST
    Formato de respuest: JSON
    '''
    if request.method == 'POST':
        leads_serializer = LeadsSerializer(data=request.data)
        if leads_serializer.is_valid():
            leads_serializer.save()
            email_de = leads_serializer.data['email']

            name = leads_serializer.data['fullname']
            mesaje = 'Lead creado con exito'
            mensaje = f"De {name}\nEmail: {email_de}\n{mesaje}"
            asunto = 'Creacion de Lead'
            email_para = ['lucianocanales@gmail.com', email_de]
            send_mail(asunto, mensaje, email_de, email_para)
            return Response(
                leads_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                leads_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
