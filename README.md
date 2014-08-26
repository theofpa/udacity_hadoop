use the following command to execute (assuming the access_log is located in myinput directory) :

```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.3.0-cdh5.1.0.jar -file ./mapper.py -mapper ./mapper.py -file ./reducer.py -reducer ./reducer.py -input myinput -output output1
```
