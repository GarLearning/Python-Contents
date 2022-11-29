# Schematics is a Python library to combine types into structures, validate them,
# and transform the shapes of your data based on simple descriptions.

from schematics.models import Model
from schematics.types import StringType, URLType
import json


class Person(Model):
    name = StringType(required=True)
    website = URLType()


# person = Person({
#     "name": "Marcos",
#     "website": "https://github.com/schematics/schematics"
# })

# print(person.name)
# print(json.dumps(person.to_primitive()))

person = Person()
person.name = "Test"
person.website = 'http://www.amontobin.com/'
print(person.validate())
