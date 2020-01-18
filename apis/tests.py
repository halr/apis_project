# from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Thing
from .serializers import ThingSerializer

# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_thing(name="", location=""):
        if name != "" and location != "":
            Thing.objects.create(name=name, location=location)

    def setUp(self):
        # add test data
        self.create_thing("MKR1000", "front room")
        self.create_thing("AIY Voice", "middle room")
        self.create_thing("AIY Vision", "backyard")
        self.create_thing("FIO", "middle room")

class GetAllThingsTest(BaseViewTest):

    def test_get_all_things(self):
        """
        This test ensures that all things added in the setUp method
        exist when we make a GET request to the things/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("things-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Thing.objects.all()
        serialized = ThingSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)