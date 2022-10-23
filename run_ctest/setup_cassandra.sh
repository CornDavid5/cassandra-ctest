#!/bin/bash

[ ! -d "app/cassandra" ] && git clone https://github.com/apache/cassandra.git app/cassandra
cd app/cassandra
git checkout 4e1d31e
git apply ../../ctest-injection.patch
CASSANDRA_USE_JDK11=true ant