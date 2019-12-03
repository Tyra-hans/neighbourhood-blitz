from django.test import TestCase
from .models import Neighbourhood

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.neighbourhood = Neighbourhood(name='Southc', location='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_save_method(self):
        self.neighbourhood.create_neighbourhood()
        neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods)>0)
    
    def test_delete_method(self):
        self.neighbourhood.create_neighbourhood()
        self.neighbourhood.delete_neighbourhood()
        neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods)is 0)