from django.urls import path

from .viewsets import library_filter_view, library_abm_view
from .viewsets import libros_abm_view, autores_abm_view
from .viewsets import leads_create_view, libro_buscar_view


urlpatterns = [
    path(
        'library/<int:pk_library>/',
        library_abm_view,
        name='libreria_abm'
    ),
    path(
        'library/<int:pk_library>/books/<int:pk_book>/',
        library_filter_view,
        name='libreria_filtro'
    ),
    path(
        'book/<int:pk>/',
        libros_abm_view,
        name='book_abm'
    ),
    path(
        'book/search',
        libro_buscar_view,
        name='book_search'
    ),
    path(
        'author/<int:pk>/',
        autores_abm_view,
        name='author_abm'
    ),
    path(
        'lead/',
        leads_create_view,
        name='lead_post'
    ),

]
