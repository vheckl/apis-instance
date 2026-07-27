from django.core.management.base import BaseCommand
from apis_instance.models import Person
import pandas as pd

class Command(BaseCommand):
    help = "imports entities and relations from CSV files"

    def handle(self, *args, **options):
        Person.objects.all().delete()
        
        persons_df = pd.read_csv("table_person_data.csv")
        self.stdout.write(f"Loaded {len(persons_df)} persons")

        for _, row in persons_df.head(10).iterrows():
            Person.objects.create(forename=row["Vorname"], 
                                  surname=row["Name"], 
                                  gender=row["Geschlecht"])

        self.stdout.write("Done")