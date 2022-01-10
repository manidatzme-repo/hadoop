#!/usr/bin/python
import pyspark
sc = pyspark.SparkContext()
text_file = sc.textFile("hdfs://localhost:9000/tmp/abc.txt")
counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("hdfs://localhost:9000/manish/output")
