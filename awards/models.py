from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_countries.fields import CountryField
from taggit.managers import TaggableManager
from django.http import Http404
from django.db.models import ObjectDoesNotExist

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
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
    site_url = models.URLField(default='https://www.google.com')
    country = CountryField(blank_label='(Chose a Country)', default='KE')
    tags = TaggableManager( help_text='A comma-separated list of tags.')
    site_description = models.TextField()
    site_image = models.ImageField(upload_to="media/user_directory_path", verbose_name="Picture", default='default.jpg')
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    # author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')

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
    def search_site(cls, search_term):
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

class Rates(models.Model):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    site = models.ForeignKey(Sites,on_delete=models.CASCADE,null=True)
    design =models.IntegerField(choices=RATE_CHOICES, default=0,blank=False)
    content =models.IntegerField(choices=RATE_CHOICES, default=0,blank=False)
    usability =models.IntegerField(choices=RATE_CHOICES, default=0,blank=False)
    average = models.DecimalField(default=1, blank=False, decimal_places=2, max_digits=40)
    date = models.DateTimeField(auto_now_add =True)


    def save_rating(self):
        self.save()
    @classmethod
    def get_ratings(cls, id):
        ratings = Rates.objects.filter(post_id=id).all()
        return ratings
    def __str__(self):
        return f'{self.site} Rating'

        
    
