#!/usr/bin/env bash

readonly LOCALSTACK_SQS_URL=http://localhost:4566

sleep 5;

set -x

aws configure set aws_access_key_id foo
aws configure set aws_secret_access_key bar
echo "[default]" > ~/.aws/config
echo "region = us-east-1" >> ~/.aws/config
echo "output = json" >> ~/.aws/config


aws --endpoint-url $LOCALSTACK_SQS_URL sqs create-queue --queue-name calculation-queue

set +x