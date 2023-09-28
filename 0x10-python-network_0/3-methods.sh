#!/bin/bash
# takes in a URL, sends a request to that URL,
curl -SI $1 | grep -i Access-Control-Allow-Methods | awk '{print $2}'
