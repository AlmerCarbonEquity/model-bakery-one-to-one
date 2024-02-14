from model_bakery.recipe import Recipe
from django.contrib.auth.models import User
from .models import Person
from .models import Profile
from model_bakery.recipe import foreign_key

user = Recipe(User)

person = Recipe(Person)

profile = Recipe(Profile)  

user_with_person = user.extend(person=foreign_key(person))