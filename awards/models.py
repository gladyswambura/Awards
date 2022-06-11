from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_countries.fields import CountryField
from taggit.managers import TaggableManager
from django.http import Http404
from django.db.models import ObjectDoesNotExist

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def save_profile(self):
        self.save()
        
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def delete_profile(self):
        self.delete()


    def __str__(self):
        return f'{self.user.username} -profile'

class Sites(models.Model):
    site_name = models.CharField(max_length=255)
    site_url = models.URLField()
    country = CountryField(blank_label='(Chose a Country)', default='KE')
    tags = TaggableManager()
    site_description = models.TextField()
    site_image = models.ImageField(upload_to = 'images/', default='images/default.jpg')
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')

    def save_site(self):
        self.save()
    
    def delete_site(self):
        self.delete()

    @classmethod
    def get_sites(cls):
        sites = cls.objects.all()
        return sites

    @classmethod
    def get_site(request, id):
        try:
            site = Sites.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return site
    
    @classmethod
    def search_sites(cls, search_term):
        sites = cls.objects.filter(site_name__icontains=search_term)
        return sites

    @classmethod
    def get_by_author(cls, author):
        sites = cls.objects.filter(author=author)
        return sites

    def __str__(self):
        return self.site_name

    class Meta:
        ordering = ['-pub_date']
    
