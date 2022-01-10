#!/usr/bin/python
import pyspark
sc = pyspark.SparkContext()
text_file = sc.textFile("hdfs:///tmp/abc.txt")
counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("hdfs:///manish/output")