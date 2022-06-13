import unittest
from django.test import TestCase
from .models import *

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='arinahgladoo', password='arinah12345')

    #First test 
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    #Second test
    def test_save_user(self):
        self.user.save()

    #Third test
    def test_delete_user(self):
        self.user.delete()

class SitesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='arinahgladoo', password='arinah12345')
        self.site = Sites.objects.create(id=1, name='test site', site_image='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='desc',
                                        user=self.user, url='http://ur.coml')

    def test_save_site(self):
        self.site.save_site()
        site = Sites.objects.all()
        self.assertTrue(len(site) > 0)

    def test_get_sites(self):
        self.site.save()
        sites = Sites.all_sites()
        self.assertTrue(len(sites) > 0)

    def test_search_site(self):
        self.site.save()
        site = Sites.search_project('test')
        self.assertTrue(len(site) > 0)

    def test_delete_site(self):
        self.site.delete_site()
        site = Sites.search_project('test')
        self.assertTrue(len(site) < 1)


class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='cate')
        self.site = Sites.objects.create(id=1, title='test site', photo='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='desc',
                                        user=self.user, url='http://ur.coml')
        self.rating = Rates.objects.create(id=1, design=6, usability=7, content=9, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rates))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rates.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_post_rating(self, id):
        self.rating.save()
        rating = Rates.get_ratings(post_id=id)
        self.assertTrue(len(rating) == 1)

if __name__ == '__main__':
    unittest.main()