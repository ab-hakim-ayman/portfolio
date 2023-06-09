from django.db import models
from django.template.defaultfilters import slugify
from PIL import Image


# Create your models here.
class About(models.Model):
    STATUS = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available')
    )
    name = models.CharField(max_length=25)
    profession = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='about', default='default/about.jpg')
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    degree = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    freelance = models.CharField(max_length=50, choices=STATUS, default=STATUS[0])
    introduction = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(About, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
class Education(models.Model):
    degree = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    session = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.degree
    
class Experience(models.Model):
    title = models.CharField(max_length=50)
    institute = models.CharField(max_length=100)
    session = models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project', default='default/project.jpg')
    url = models.URLField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Skill(models.Model):
    TAGS = (
        ('expert', 'Expert'),
        ('proficient', 'Proficient'),
        ('competent', 'Competent'),
        ('advanced Beginner', 'Advanced Begineer'),
        ('novice', 'Novice')
    )
    name = models.CharField(max_length=30)
    level = models.IntegerField(default=50)
    tag = models.CharField(max_length=50, choices=TAGS, default=TAGS[2])
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    author = models.CharField(max_length=25)
    author_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonial', default='default/testimonial.jpg')
    quotation = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
    
class Social(models.Model):
    name = models.CharField(max_length=25, unique=True)
    icon = models.CharField(max_length=50, unique=True)
    url = models.URLField(max_length=200, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Achievement(models.Model):
    institute = models.CharField(max_length=75)
    title = models.CharField(max_length=250, unique=True)
    url = models.URLField(unique=True)
    introduction = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name