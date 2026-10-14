FROM postgres:16-bookworm
# postgis/postgis has no arm64 build, so add PostGIS and pgvector to the
# official multi-arch image (it already has the PostgreSQL apt repo configured).
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      postgresql-16-postgis-3 \
      postgresql-16-pgvector \
 && rm -rf /var/lib/apt/lists/*
