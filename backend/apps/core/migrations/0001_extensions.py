from django.contrib.postgres.operations import CreateExtension
from django.db import migrations
from pgvector.django import VectorExtension


class Migration(migrations.Migration):
    """Enable PostGIS and pgvector. Migrations that add spatial or vector
    fields should depend on this one."""

    initial = True
    dependencies = []

    operations = [
        CreateExtension("postgis"),
        VectorExtension(),
    ]
