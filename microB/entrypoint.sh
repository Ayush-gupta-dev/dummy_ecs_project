#!/bin/bash

# Run the consumer in the background
python consumer.py &

# Run the API server
uvicorn api:app --host 0.0.0.0 --port 8001
