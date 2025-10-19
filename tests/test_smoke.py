from django.test import TestCase


class SmokeTest(TestCase):
    def test_truth(self):
        assert 1 + 1 == 2
