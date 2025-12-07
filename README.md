# Automated Reporting System (Demo)

## Overview
This repository demonstrates an automated ETL and reporting pipeline designed to generate and distribute periodic energy usage reports (Daily, Weekly, Monthly). The system fetches raw telemetry data from a MySQL database, performs aggregation using **Pandas**, generates Excel files, and dispatches them via SMTP email.

> **Note:** Specific report templates (Excel formatting) and proprietary SQL queries have been simplified for this demonstration to comply with confidentiality agreements.

## 🏗️ Architecture

1.  **Data Extraction**: `utils/db_connector.py` handles secure database connections and executes SQL queries.
2.  **Data Transformation**: Report modules (e.g., `reports/daily_report.py`) use **Pandas** to clean, group, and aggregate time-series data.
3.  **Delivery**: `utils/email_sender.py` manages SMTP connections to deliver generated artifacts to stakeholders.
4.  **Scheduling**: `main_scheduler.py` serves as the entry point, designed to be triggered by system schedulers (e.g., Linux Cron or Windows Task Scheduler).

## 🚀 Key Features

*   **Pandas-based ETL**: Efficiently handles large datasets for aggregation (Sum, Max, Average) without loading DB servers.
*   **Modular Design**: Separate modules for different report frequencies allow for easy maintenance and extension.
*   **Automated Delivery**: Integration with SMTP ensures stakeholders receive timely insights without manual intervention.

## Usage

Run a daily report generation task:
  ```
  python main_scheduler.py --type daily
  ```

## Tech Stack
*   Python 3
*   Pandas (Data Analysis)
*   PyMySQL (Database Driver)
*   smtplib (Email)
