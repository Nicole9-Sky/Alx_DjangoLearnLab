from rest_framework import serializers 
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelsSerializer):
    class Meta:
        model = Body
        fields = '__all__'
    
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("publication year cannot be iin the future ")     
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'Book']
        
from rest_framework import serializers 
from .models import Author, Book 
from datetime import datetime 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'Book']
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validation_publication_year(self, value):
        current_year = datetime.now().year 
        if value > current_year:
            raise serializers.ValidationError("publication year cannot be in the future")
        return value 
            
            