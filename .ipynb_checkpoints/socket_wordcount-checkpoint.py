from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create a SparkContext
sc = SparkContext(appName="SocketWordCount")
sc.setLogLevel("WARN")  # Reduce verbosity

# Set the batch interval to 1 second
batch_interval = 1
ssc = StreamingContext(sc, batch_interval)

# Create a DStream that will connect to localhost:9999
lines = ssc.socketTextStream("localhost", 9999)

# Split each line into words
words = lines.flatMap(lambda line: line.split(" "))

# Count each word in each batch
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Print the word counts of each batch
wordCounts.pprint()

# Start the streaming context
ssc.start()

# Wait for the streaming to be stopped
ssc.awaitTermination()