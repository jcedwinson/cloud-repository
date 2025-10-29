# movies/views.py
from rest_framework import generics, filters
from .models import Movie
from .serializers import MovieSerializer


# LIST + CREATE + SEARCH + ORDERING
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    #Enable search and ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'actor', 'actress', 'genre']  # searchable fields
    ordering_fields = ['release_year', 'rating']  # sortable fields
    ordering = ['release_year']  # default ordering


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
