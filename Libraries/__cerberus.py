# Cerberus provides powerful yet simple and lightweight data validation functionality out of the box
# and is designed to be easily extensible, allowing for custom validation.

from cerberus import Validator

schema = {"name": {"type": "string"},
          "age": {"type": "integer"}
          }

v = Validator(schema)

name = "test"
age = 21

document = {"name": input("say your name: ")}

print(v.validate(document))
