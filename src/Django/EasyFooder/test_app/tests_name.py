from django.test import TestCase

class TestTestCase(TestCase):
    def setUp(self):
        def function(a, b):
            return a+b

    def test_animals_can_speak(self):
        a = 5
        b = 2
        self.assertEqual(a+b, 7)
