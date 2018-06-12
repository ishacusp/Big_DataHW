#!/bin/bash

#Extra Credit: This shell script runs three map-reduce jobs. The input of the first job is the original text file
#while the input of the second job is the part-00000 file from the output of the first job. 
#Similarly, the third job takes in the output of the second job. 
#All the three jobs stores the output into three different output locations.

hadoop jar /opt/cloudera/parcels/CDH-5.11.1-1.cdh5.11.1.p0.4/lib/hadoop-mapreduce/hadoop-streaming.jar -D mapreduce.job.reduces=1 -files hdfs://dumbo/user/ic1018/class3/python_code/pagerank_mapper.py,hdfs://dumbo/user/ic1018/class3/python_code/pagerank_reducer_1.py -mapper "python pagerank_mapper.py" -reducer "python pagerank_reducer_1.py" -input /user/ic1018/class3/pagerank_input.txt -output /user/ic1018/class3/output

hadoop jar /opt/cloudera/parcels/CDH-5.11.1-1.cdh5.11.1.p0.4/lib/hadoop-mapreduce/hadoop-streaming.jar -D mapreduce.job.reduces=1 -files hdfs://dumbo/user/ic1018/class3/python_code/pagerank_mapper.py,hdfs://dumbo/user/ic1018/class3/python_code/pagerank_reducer_1.py -mapper "python pagerank_mapper.py" -reducer "python pagerank_reducer_1.py" -input /user/ic1018/class3/output/part-00000 -output /user/ic1018/class3/output2

hadoop jar /opt/cloudera/parcels/CDH-5.11.1-1.cdh5.11.1.p0.4/lib/hadoop-mapreduce/hadoop-streaming.jar -D mapreduce.job.reduces=1 -files hdfs://dumbo/user/ic1018/class3/python_code/pagerank_mapper.py,hdfs://dumbo/user/ic1018/class3/python_code/pagerank_reducer_1.py -mapper "python pagerank_mapper.py" -reducer "python pagerank_reducer_1.py" -input /user/ic1018/class3/output2/part-00000 -output /user/ic1018/class3/output3

