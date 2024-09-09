from django.test import TestCase
from .models import Document

# Create your tests here.


class SearchTests(TestCase):
    def setUp(self):
        Document.objects.create(
            title="Test Document 1", content="This is a test document."
        )
        Document.objects.create(title="Another Test", content="Another Test Document.")

    def test_search(self):
        response = self.client.get("/search/?q=test")
        self.assertContains(response, "Test Document 1")
        self.assertContains(response, "Another Test")
