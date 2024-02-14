from django.test import TestCase
from .baker_recipes import user_with_person
from django.contrib.auth.models import User

class UserWithPersonTest(TestCase):
    def setUp(self):
        self.user_with_person = user_with_person.make()

    def test_user_with_person_creation(self):
        self.assertIsNotNone(self.user_with_person.person.id)
        self.assertIsNotNone(User.objects.get(id=self.user_with_person.id).person.id)