from django.test import TestCase
# Create your tests here.
# Example - add strings
'''
def demo(str1,str2):
    return str1 + str2
class Testdemo(TestCase):
    def test_concate(self):
        self.assertEquals(demo("hello","world"),"helloworld")
'''
# add 2 numbers
'''
def demo(a,b):
    return 5 + 10
class Testdemo(TestCase):
    def test_concate(self):
        self.assertEquals(demo(5,10),15)
'''
# Example

def get_max(num1,num2):
    return num1 if num1 > num2 else num2
class TestDemo(TestCase):
    def test_get_max(self):
        self.assertEquals(get_max(5,8),8)
