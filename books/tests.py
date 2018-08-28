from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Book


class AddBooksTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = {
            'title': 'book',
            'author': 'author',
            'summary': 'summary',
            'no_pages': 10,
            'complete': True,
        }

    def test_add_book_that_you_have_completed(self):
        response = self.client.post(reverse('add-book'), data=self.book)
        book = Book.objects.get(pk=1)
        self.assertEqual(book.current_page, book.no_pages)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_book_marked_as_incomplete_without_current_page(self):
        self.book['complete'] = False
        response = self.client.post(reverse('add-book'), data=self.book)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateBooksTestCase(TestCase):
    book_id = None
    def setUp(self):
        self.client = APIClient()
        self.book = {
            'title': 'book',
            'author': 'author',
            'summary': 'summary',
            'no_pages': 10,
            'current_page': 5
        }
        self.book_id = Book.objects.create(**self.book).id
        
    def test_update_unexisting_book(self):
        response = self.client.put(reverse('update-book', kwargs={'id': 2}), data={'no_pages': 7})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_book_before_completing(self):
        response = self.client.put(reverse('update-book', kwargs={'id': self.book_id}), data={'current_page': 7})
        self.assertEqual(response.data['current_page'], 7)
        self.assertFalse(response.data['complete'])

    def test_update_book_after_completing(self):
        response = self.client.put(reverse('update-book', kwargs={'id': self.book_id}), data={'current_page': 10})
        self.assertEqual(response.data['current_page'], 10)
        self.assertTrue(response.data['complete'])

    def test_update_for_complete_book(self):
        self.client.put(reverse('update-book', kwargs={'id': self.book_id}), data={'current_page': 10})
        response = self.client.put(reverse('update-book', kwargs={'id': self.book_id}), data={'current_page': 6})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
