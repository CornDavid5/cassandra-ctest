#!/bin/bash

[ ! -d "../app/cassandra" ] && git clone https://github.com/apache/cassandra.git ../app/cassandra
cd ../app/cassandra
git checkout 4e1d31e
git apply ../../ctest-logging.patch
CASSANDRA_USE_JDK11=true ant