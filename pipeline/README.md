# 🚕 NYC Taxi Data Pipeline (Docker + Postgres + Ingestion)
This project sets up a reproducible data pipeline that:
- Spins up a PostgreSQL database + pgAdmin using Docker Compose
- Builds a Python ingestion pipeline using Docker
- Loads NYC taxi CSV data into Postgres tables

---

## 📦 Project Components
- **docker-compose.yml** → runs infrastructure (Postgres + pgAdmin)
- **Dockerfile** → builds ingestion pipeline image
- **ingest_data.py** → reads CSV, transforms, loads into Postgres
- **Postgres volume** → persists database data

---

# 🚀 1. Start the Database (Postgres + pgAdmin)
Run:
```bash
docker compose up -d
```

# 🔑 pgAdmin login
Email: admin@admin.com
Password: root

# 🚕 2. Build Ingestion Docker Image
Build the ingestion pipeline image:
```bash
docker build -t taxi_ingest:v001 .
```

# ▶️ 3. Run Data Ingestion Pipeline
Example run:
``` bash
docker run -it --rm \
  --network=pipeline_default \
  taxi_ingest:v001 \
  --pg-user=root \
  --pg-pass=root \
  --pg-host=pgdatabase \
  --pg-port=5432 \
  --pg-db=ny_taxi \
  --year=2021 \
  --month=1 \
  --chunksize=100000 \
  --target-table=yellow_taxi_trips_2021_01
```

# 🛑 6. Stop Everything
Stop services:
``` bash 
docker compose down
```

# ⚠️ WARNING
DO NOT use:
```bash
docker compose down -v
```


# Cleanup (OPTIONAL)
```bash
docker ps -a
docker rm <container_id>
docker rmi <image_name>
```