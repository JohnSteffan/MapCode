#!/bin/bash
hadoop jar /usr/hdp/2.5.0.0-1245/hadoop-mapreduce/hadoop-streaming.jar \
-file practice/autoinc_mapper1.py -mapper /practice/autoinc_mapper1.py \
-file practice/autoinc_reducer1.py -reducer /practice/autoinc_reducer1.py \
-input /data/data.csv -output /output_files/all_accidents
hadoop jar /usr/hdp/2.5.0.0-1245/hadoop-mapreduce/hadoop-streaming.jar \
-file practice/autoinc_mapper2.py -mapper "python autoinc_mapper2.py" \
-file practice/autoinc_reducer2.py -reducer "python autoinc_reducer2.py" \
-input /output_files/all_accidents -output /output_files/make_year_count

