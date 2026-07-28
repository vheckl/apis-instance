# APIS Instance

An APIS (Austrian Prosopographical Information System) instance,
built to model and import data from the SiCProD project
(https://sicprod.acdh.oeaw.ac.at/), as part of a Digital Humanities
internship at ACDH.

## What's here

- A minimal ontology: `Person` (based on APIS's `E21_Person`) and
  `IsMarriedTo`, a relation connecting two people.
- An import script (`manage.py import_sicprod`) that loads SiCProD person
  and marriage data into the instance.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
uv sync
uv run manage.py migrate
uv run manage.py createsuperuser
uv run manage.py runserver
```

## Importing data

```bash
uv run manage.py import_sicprod
```

This imports all persons from `table_person_data.csv` and all marriage
relations from `table_marriages.csv`.

## Data

`table_person_data.csv` and `table_marriages.csv` contain data derived from
the SiCProD project.
