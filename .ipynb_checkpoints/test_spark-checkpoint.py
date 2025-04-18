from pyspark.sql import SparkSession

print("Starting SparkSession creation...")
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("TestApp") \
    .getOrCreate()

print("SparkSession created successfully!")