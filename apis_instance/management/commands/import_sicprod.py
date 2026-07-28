from django.core.management.base import BaseCommand
from apis_instance.models import Person, IsMarriedTo
import pandas as pd

class Command(BaseCommand):
    help = "imports entities and relations from CSV files"

    def handle(self, *args, **options):
        IsMarriedTo.objects.all().delete()
        Person.objects.all().delete()

        persons_df = pd.read_csv("table_person_data.csv")
        self.stdout.write(f"Loaded {len(persons_df)} persons")

        person_lookup = {}

        for _, row in persons_df.iterrows():
            person = Person.objects.create(forename=row["Vorname"], 
                                  surname=row["Name"], 
                                  gender=row["Geschlecht"])
            person_lookup[row["ID"]] = person

        self.stdout.write(f"Lookup has {len(person_lookup)} entries")
        self.stdout.write("Done")

        marriages_df = pd.read_csv("table_marriages.csv")
        self.stdout.write(f"Loaded {len(marriages_df)} marriage records")

        for _, row in marriages_df.iterrows():
            if row["Subj object id"] == row["Obj object id"]:
                continue

            subj_person = person_lookup[row["Subj object id"]]
            obj_person = person_lookup[row["Obj object id"]]

            IsMarriedTo.objects.create(subj=subj_person, obj=obj_person)