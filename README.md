## Real-Time Healthcare Data Processing with Delta Live Tables (DLT) in Databricks

### Problem Statement
This project aims to create a robust data pipeline for processing real-time healthcare data using Delta Live Tables (DLT) in Databricks. The goal is to ingest raw patient data and transform it into different Delta tables (Bronze, Silver, and Gold) for efficient storage, analysis, and processing.

### Tech Stack
- **PySpark**
- **Databricks**
- **Delta Tables**
- **Databricks DLT Workflow**

### Project Overview
1. **Feed Real-Time Patient Data**: Use PySpark to ingest real-time patient data into a raw Delta table.
2. **Create Bronze, Silver, and Gold Delta Live Tables**: Use a PySpark notebook to build DLT workflows that transform data at different stages.
3. **DLT Pipeline Workflow**: Set up a Delta Live Table workflow in Databricks for continuous data processing.

### Project Structure
- **`docs/`**: Contains documentation and diagrams detailing the project architecture and workflow.
- **`src/`**: Source code for feeding data, creating Delta Live Tables, and the DLT workflow configuration.
- **`tests/`**: Unit tests for ensuring data quality and integrity.
- **`notebooks/`**: Jupyter or Databricks notebooks used in the project.
- **`data/`**: Contains sample data files for testing.

### Installation and Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/healthcare-dlt-pipeline.git
