from django.db import models

# from django.db.models.deletion import CASCADE

# Create your models here.
class Editor(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.CharField(max_length=12,blank=True)

    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        self.save()
    
    def delete_editor(self):
        self.save()

    def update_editor(self):
        self.save()

# creating a tag models in our database
class tag(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    def save_tag(self):
        self.save()
    
    def delete_tag(self):
        self.save()

    def update_tag(self):
        self.save()

# creating a Article models in our database
class Article(models.Model):
    title=models.CharField(max_length=30)
    post=models.TextField()
    editor=models.ForeignKey(Editor,on_delete=models.CASCADE)
    tags=models.ManyToManyField(tag)
    pub_date=models.DateTimeField(auto_now_add=True)
    article_image=models.ImageField(upload_to='gallary/')


    def __str__(self):
        return self.post

    def save_Article(self):
        self.save()
    
    def delete_Article(self):
        self.save()

    def update_Article(self):
        self.save()






    