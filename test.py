# create the first pyspark code
# create a connection by local server "standalone"
# the driver program, spark shell itself, lanching various parallel operations on a cluster. 
# sc: SparkContext object, the driver program access spark through this object
#  


from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("wordCount")
sc = SparkContext(conf)

input = sc.textFile(inputFile)
words = input.flatMap(lambda line: line.split(" "))
counts = words.map(lambda word: (word,1)).reduceByKey(lambda x,y: x+y)
counts.saveAsTextFile(outputFile)
