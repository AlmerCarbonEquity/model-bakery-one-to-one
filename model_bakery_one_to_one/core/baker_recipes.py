from model_bakery.recipe import Recipe
from django.contrib.auth.models import User
from .models import Person
from model_bakery.recipe import foreign_key

user = Recipe(User)

person = Recipe(Person)

user_with_person = user.extend(person=foreign_key(person))