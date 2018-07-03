hw5_script.pig

A  = LOAD 'hdfs://dumbo/user/ic1018/class4/word_input.txt' USING PigStorage() AS(line:Chararray);

B = FOREACH A GENERATE LOWER(line) as lower_line;

C = FOREACH B GENERATE ((lower_line matches '.*hackathon.*'? 1:0)) as t1,((lower_line matches '.*dec.*'?1:0)) as t2,((lower_line matches '.*java.*'?1:0)) as t3,((lower_line  matches '.*chicago.*'?1:0)) as t4;

D = GROUP C ALL;

E  = FOREACH D GENERATE FLATTEN(TOBAG(CONCAT('Chicago',' ',(chararray)SUM(C.t4)),CONCAT('Dec',' ',(chararray)SUM(C.t2)),CONCAT('Java',' ',(chararray)SUM(C.t3)),CONCAT('hackathon',' ',(chararray)SUM(C.t1))));

DUMP E;