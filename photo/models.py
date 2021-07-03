from django.db import models
# from django.db.models.deletion import CASCADE

# Create your models here.
class Editor(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()

    def __str__(self):
        return self.first_name
    class meta:
        ordering=['first_name']

# creating a tag models in our database
class tag(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

# creating a Article models in our database
class Article(models.Model):
    title=models.CharField(max_length=30)
    post=models.TextField()
    editor=models.ForeignKey(Editor)
    tags=models.ManyToManyField(tag)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post