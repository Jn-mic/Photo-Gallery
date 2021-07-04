from django.test import TestCase
from .models import Editor, tag, Article

# Create your tests here.
class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.Moringa= Editor(first_name='Moringa',last_name='student',email='ms@moringa.ke')

    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Moringa, Editor))

    # Testing save method

    def test_save_method(self):
        self.Moringa.save_editor()
        editors= Editor.objects.all()
        self.assertTrue(len(editors)>0)

    # Testing delete method
    def test_delete_method(self):
        self.Moringa.delete_editor()
        editors= Editor.objects.all()
        self.assertTrue(len(editors)>0)

    # Testing update method
    def test_update_method(self):
        self.Moringa.update_editor()
        editors= Editor.objects.all()
        self.assertTrue(len(editors)>0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.name=tag(tag_name='tech')
    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.name, tag))

    def test_save_method(self):
        self.name.save_tag()
        tags= tag.objects.all()
        self.assertTrue(len(tags)>0)
    
    def test_delete_method(self):
        self.name.save_tag()
        tags= tag.objects.all()
        self.assertTrue(len(tags)>0)

    def test_update_method(self):
        self.name.save_tag()
        tags= tag.objects.all()
        self.assertTrue(len(tags)>0)

# Article Test.
class ImageTestClass(TestCase):
    #set up method
    def setUp(self):
        self.Technology= Article(title='DATA-SCIENCE',Post='Review',editor='Jimmy')

    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Technology, Article))

    # Testing save method

    def test_save_method(self):
        self.Technology.save_article()
        article= Article.objects.all()
        self.assertTrue(len(article)>0)

    # Testing delete method
    def test_delete_method(self):
        self.Technology.delete_article()
        article= Article.objects.all()
        self.assertTrue(len(article)>0)

    # Testing update method
    def test_update_method(self):
        self.Technology.update_article()
        article= Article.objects.all()
        self.assertTrue(len(article)>0)


    