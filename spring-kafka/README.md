# Spring Boot with Kafka Consumer

# change directory to kafka for example (version may differ): 
- `cd Downloads/kafka_2.13-3.0.0/`

## Start Zookeeper
- `bin/zookeeper-server-start.sh config/zookeeper.properties`

## Start Kafka Server
- `bin/kafka-server-start.sh config/server.properties`

## Create Kafka Topic
- `bin/kafka-topics.sh --create --topic KafkaEx --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1`
- `bin/kafka-topics.sh --create --topic samplekafka --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1`

## Publish to the Kafka Topic via Console
- `bin/kafka-console-producer.sh --topic KafkaEx --bootstrap-server localhost:9092`
- `bin/kafka-console-producer.sh --topic samplekafka --bootstrap-server localhost:9092`

## eg for sampleKafka to produce for ticker details in stock market
-`{"symbol":"Titan", "open":23800.00}`

-`{"symbol":"Titan", "open":23800.00, "high":2422.65, "low":2360.30, "close":2384.00, "oi":1125, "vol":372255}`
#some are commented

## KafkaTopic in case need to pass any valid messages alone 
-`bin/kafka-console-producer.sh --topic KafkaEx --bootstrap-server localhost:9092`
eg: -`hello Tealvue!`

