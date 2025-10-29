from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = [
        ("Action", "Action"),
        ("Drama", "Drama"),
        ("Comedy", "Comedy"),
        ("Thriller", "Thriller"),
        ("Horror", "Horror"),
        ("Romance", "Romance"),
        ("Sci-Fi", "Sci-Fi"),
    ]

    name = models.CharField(max_length=200)
    actor = models.CharField(max_length=150)
    actress = models.CharField(max_length=150, blank=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    release_year = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)  
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-release_year", "name"]

    def __str__(self):
        return f"{self.name} ({self.release_year})"
