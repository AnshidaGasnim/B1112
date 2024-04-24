# Two types of Testing.  1- Unit testing  2- Integration testing
# Unit testing- URL testing:- there are two ways
# URL testing using client instance
from django.test import TestCase
'''
class Testurl(TestCase):
    def test_home(self):
        response=self.client.get('/')          # home page path is empty.bcz grt('/).
        print(response)
        self.assertEquals(response.status_code,200)
'''
# URL testing using Reverse and Resolve method
from django.urls import reverse,resolve
from shop import views
from shop.views import *

class TestUrl(TestCase):
    def test_home(self):
        myurl=reverse('home')
        print("url is", myurl)
        self.assertEquals(resolve(myurl).func, home)
        print(resolve(myurl))