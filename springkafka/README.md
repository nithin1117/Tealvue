# Spring Boot with Kafka Consumer
#change directory to kafka for example use version accordingly:
-`cd Downloads/kafka_2.13-3.0.0/`


## Start Zookeeper
-`bin/zookeeper-server-start.sh config/zookeeper.properties`


## Start Kafka Server
-`bin/kafka-server-start.sh config/server.properties`


## Create Kafka Topic for ubuntu
-`bin/kafka-topics.sh --create --topic KafkaExample --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1`
-`bin/kafka-topics.sh --create --topic sampleKafka --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1`



## Publish to the Kafka Topic via Console
-`bin/kafka-console-producer.sh --topic sampleKafka --bootstrap-server localhost:9092`

#eg for sampleKafka producer:
-`{"symbol":"Titan", "open":23800.00}`

-`{"symbol":"Titan", "open":23800.00, "high":2422.65, "low":2360.30, "close":2384.00, "oi":1125, "vol":372255}` #some are commented



#KafkaTopic in case need to pass any valid messages alone

-`bin/kafka-console-producer.sh --topic KafkaExample --bootstrap-server localhost:9092`

#eg:
-`hello Tealvue!`






