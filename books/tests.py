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
            'category': 'art'
        }
        self.user = User.objects.create_user(username='username', password='password')
        self.book['owner'] = self.user

    def test_add_book_that_you_have_completed(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(reverse('add-book'), data=self.book)
        book = Book.objects.get(pk=1)
        self.assertEqual(book.current_page, book.no_pages)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_book_marked_as_incomplete_without_current_page(self):
        self.client.force_authenticate(self.user)
        del self.book['complete']
        response = self.client.post(reverse('add-book'), data=self.book)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_current_page_greater_than_no_pages(self):
        self.client.force_authenticate(self.user)
        del self.book['complete']
        self.book['current_page'] = 15
        response = self.client.post(reverse('add-book'), data=self.book)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_current_page_is_equal_to_no_pages(self):
        self.client.force_authenticate(self.user)
        del self.book['complete']
        self.book['current_page'] = 15
        response = self.client.post(reverse('add-book'), data=self.book)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_book_unauthenticated_user(self):
        response = self.client.post(reverse('add-book'), data=self.book)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


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
        self.user = User.objects.create_user(username='username', password='password')
        self.book['owner'] = self.user
        self.book_id = Book.objects.create(**self.book).id

    def test_update_unexisting_book(self):
        self.client.force_authenticate(self.user)
        response = self.client.put(reverse('update-book', kwargs={'id': 2}), data={'no_pages': 7})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_book_before_completing(self):
        self.client.force_authenticate(self.user)
        response = self.client.put(reverse('update-book', kwargs={'id': self.book_id}), data={'current_page': 7})
        self.assertEqual(response.data['current_page'], 7)
        self.assertFalse(response.data['complete'])

    def test_update_book_after_completing(self):
        self.client.force_authenticate(self.user)
        response = self.client.put(reverse('update-book', kwargs={'id': self.book_id}), data={'current_page': 10})
        self.assertEqual(response.data['current_page'], 10)
        self.assertTrue(response.data['complete'])

    def test_update_for_complete_book(self):
        self.client.force_authenticate(self.user)
        self.client.put(reverse('update-book', kwargs={'id': self.book_id}), data={'current_page': 10})
        response = self.client.put(reverse('update-book', kwargs={'id': self.book_id}), data={'current_page': 6})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_another_users_book(self):
        user2 = User.objects.create_user(username='username2', password='password')
        self.client.force_authenticate(user2)
        response = self.client.put(reverse('update-book', kwargs={'id': self.book_id}), data={'current_page': 10})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user_account(self):
        self.client.post(reverse('add-user'), data= {
            'username': 'username',
            'password': 'password'
        })
        self.assertEqual(User.objects.all().count(), 1)
