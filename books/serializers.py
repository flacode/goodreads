from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        current_page = data.get('current_page')
        complete = data.get('complete')

        if not current_page and not complete:
            raise ValidationError('Please enter the current page if you have not completed the book yet.')
    
        if complete:
            data['current_page'] = data['no_pages']
        return data


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'summary', 'complete', 'current_page', 'no_pages')
        read_only_fields = ('title', 'author', 'summary', 'complete', 'no_pages')

    def validate_current_page(self, value):
        if self.instance.no_pages < value:
            raise ValidationError('Current page should be less than the number of pages')
        if self.instance.complete:
            raise ValidationError('Can not update pages for a book you have completed')
        return value

    def update(self, instance, validated_data):
        if instance.no_pages == validated_data['current_page']:
            instance.complete = True
        instance.current_page = validated_data['current_page']
        instance.save()
        return instance
