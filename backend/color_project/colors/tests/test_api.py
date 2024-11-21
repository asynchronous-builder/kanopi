from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class TestSwatchesAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_get_swatches(self):
        response = self.client.get(reverse('swatches'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)  # Default count
        
    def test_custom_count(self):
        response = self.client.get(reverse('swatches'), {'count': 3})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        
    def test_invalid_count(self):
        response = self.client.get(reverse('swatches'), {'count': -1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_max_count_limit(self):
        response = self.client.get(reverse('swatches'), {'count': 1000})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)