import pytest
from pyspark.sql import SparkSession

# Initialize SparkSession for testing
@pytest.fixture(scope="module")
def spark():
    spark = SparkSession.builder \
        .appName("Data Quality Tests") \
        .getOrCreate()
    yield spark
    spark.stop()

def test_silver_table_schema(spark):
    # Load the Silver table
    silver_df = spark.read.format("delta").table("gds_de_bootcamp.default.processed_patient_data")

    # Define expected schema
    expected_schema = {
        "patient_id": "string",
        "name": "string",
        "age": "integer",
        "gender": "string",
        "address": "string",
        "contact_number": "string",
        "admission_date": "timestamp",
        "diagnosis_description": "string"
    }

    # Check the schema of the Silver table
    for field in silver_df.schema.fields:
        assert field.dataType.simpleString() == expected_schema[field.name], f"Data type mismatch for {field.name}"

def test_gold_table_schema(spark):
    # Load the Gold tables
    gold_df1 = spark.read.format("delta").table("gds_de_bootcamp.default.patient_statistics_by_diagnosis")
    gold_df2 = spark.read.format("delta").table("gds_de_bootcamp.default.patient_statistics_by_gender")

    # Define expected schemas
    expected_schema1 = {
        "diagnosis_description": "string",
        "patient_count": "bigint",
        "avg_age": "double",
        "unique_gender_count": "bigint",
        "min_age": "integer",
        "max_age": "integer"
    }
    
    expected_schema2 = {
        "gender": "string",
        "patient_count": "bigint",
        "avg_age": "double",
        "unique_diagnosis_count": "bigint",
        "min_age": "integer",
        "max_age": "integer"
    }

    # Check the schema of the first Gold table
    for field in gold_df1.schema.fields:
        assert field.dataType.simpleString() == expected_schema1[field.name], f"Data type mismatch for {field.name} in patient_statistics_by_diagnosis"

    # Check the schema of the second Gold table
    for field in gold_df2.schema.fields:
        assert field.dataType.simpleString() == expected_schema2[field.name], f"Data type mismatch for {field.name} in patient_statistics_by_gender"

def test_no_missing_values(spark):
    # Load the Silver table
    silver_df = spark.read.format("delta").table("gds_de_bootcamp.default.processed_patient_data")

    # Check for missing values in critical columns
    assert silver_df.filter(silver_df["patient_id"].isNull()).count() == 0, "Missing values found in patient_id column"
    assert silver_df.filter(silver_df["name"].isNull()).count() == 0, "Missing values found in name column"
    assert silver_df.filter(silver_df["age"].isNull()).count() == 0, "Missing values found in age column"
    assert silver_df.filter(silver_df["gender"].isNull()).count() == 0, "Missing values found in gender column"
    assert silver_df.filter(silver_df["address"].isNull()).count() == 0, "Missing values found in address column"
    assert silver_df.filter(silver_df["contact_number"].isNull()).count() == 0, "Missing values found in contact_number column"
    assert silver_df.filter(silver_df["admission_date"].isNull()).count() == 0, "Missing values found in admission_date column"

    # Load the Gold tables
    gold_df1 = spark.read.format("delta").table("gds_de_bootcamp.default.patient_statistics_by_diagnosis")
    gold_df2 = spark.read.format("delta").table("gds_de_bootcamp.default.patient_statistics_by_gender")

    # Check for missing values in critical columns of Gold tables
    assert gold_df1.filter(gold_df1["diagnosis_description"].isNull()).count() == 0, "Missing values found in diagnosis_description column of patient_statistics_by_diagnosis"
    assert gold_df2.filter(gold_df2["gender"].isNull()).count() == 0, "Missing values found in gender column of patient_statistics_by_gender"
