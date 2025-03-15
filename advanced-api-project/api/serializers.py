from rest_framework import serializers 
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("publication year cannot be in the future.")
        return value  

    class Meta:
        model = Book
        fields = '__all__'
        
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) 
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'Book']
        

            