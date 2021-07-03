from django.test import TestCase
from .models import Editor, tag, Article

# Create your tests here.
class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.moringa= Editor(first_name='moringa',last_name='student',email='ms@moringa.com')

    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.moringa, Editor))