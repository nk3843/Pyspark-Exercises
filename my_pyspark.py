from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("MyPySparkApp").getOrCreate()

# Create a simple DataFrame
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()

# Stop the SparkSession
spark.stop()