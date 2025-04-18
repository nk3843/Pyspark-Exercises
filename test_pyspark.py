from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TestPySpark").getOrCreate()

print("PySpark is working!")

spark.stop()