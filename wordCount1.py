#wordcount1.py
#Achive wordfilter with a wordFunctions class
#Apply read arguments from terminal, apply functions created in a python class
from pyspark import SparkConf, SparkContext,RDD
import sys
#conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext("local", "WordCount")



class WordFunctions(object) :
	def __init__(self, query):
		self.query = query
	def getMatchesNoReference(self, rdd):
		query = self.query
		return rdd.filter(lambda line: query in line.lower())
		
def main(argv):
	input = argv
	rdd = sc.textFile(input)
	word = WordFunctions("spark")
	output = word.getMatchesNoReference(rdd)
	print ("input file have", rdd.count(), "lines.\n")
	print ("matched file have", output.count(), "lines.\n")
	for line in output.collect():
		print(line)

if __name__ == "__main__": 
	main(sys.argv[1])
