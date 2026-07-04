# Docker Test – Data Pipeline (Zoomcamp Module 1)

This project is part of the Data Engineering Zoomcamp Module 1.  
It demonstrates a simple data pipeline using Python, Pandas, and Parquet file output.

---

## What this project does

- Reads a command-line argument (`day`)
- Creates a small sample dataset using Pandas
- Outputs a Parquet file based on the input day
- Reads the Parquet file back to verify output

---

## Tech stack

- Python
- Pandas
- PyArrow (for Parquet support)
- Docker (optional for containerized execution)

---

## How to run

### Run locally
```bash
python pipeline_docker.py 12