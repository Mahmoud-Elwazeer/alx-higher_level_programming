#!/bin/bash
# takes in a URL, sends a request to that URL,
curl -SI $1 | grep -i Allow | awk '{print $2}'
