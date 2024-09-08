# Workflow Details: Real-Time Healthcare Data Processing

## Overview
This document describes the workflow used to process real-time healthcare data using Delta Live Tables (DLT) in Databricks.

### Bronze Layer
- **Description:** Ingests raw patient data from the source. No transformations are applied at this stage.
- **Purpose:** To keep an unaltered copy of the raw data for compliance and reprocessing needs.

### Silver Layer
- **Description:** Applies necessary transformations such as filtering, deduplication, and basic cleaning to prepare the data for analytics.
- **Purpose:** To enhance data quality and make it suitable for analytical queries.

### Gold Layer
- **Description:** Performs advanced aggregations and enrichment to create a final dataset optimized for business reporting and insights.
- **Purpose:** To provide a clean, enriched dataset ready for business consumption.

### Delta Live Tables (DLT) Workflow
- **Description:** Manages the data pipeline from raw ingestion to final reporting, ensuring continuous, reliable, and consistent data flow.
- **Configuration:** The `dlt_pipeline_workflow.json` file contains the configuration details used to automate this workflow in Databricks.
