from django.db import models
from users.models import User
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse
from django.template.defaultfilters import default
from markdown import markdown
from django.utils.html import strip_tags

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
@python_2_unicode_compatible    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100)
    
    body = models.TextField()
    
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    
    excerpt = models.CharField(max_length=200, blank=True)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    views = models.PositiveIntegerField(default = 0)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('circleblogapp:detail', kwargs={'pk':self.pk})
    
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
        
    def save(self, *args, **kwargs):
        
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                ])
            
            self.excerpt = strip_tags(md.convert(self.body))[:54]
            
        super(Post, self).save(*args, **kwargs)
