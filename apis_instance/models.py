from django.db import models
from apis_core.apis_entities.models import AbstractEntity
from apis_core.entities.abc import E21_Person, Entity
from apis_core.generic.abc import GenericModel
from apis_core.relations.models import Relation


class Person(E21_Person, AbstractEntity, Entity):
    pass


class IsMarriedTo(Relation):
    subj_model = Person
    obj_model = Person

    @classmethod
    def reverse_name(self) -> str:
        return "is married to"