#!/bin/bash
# takes in a URL, sends a GET request to the URL
curl -sw "%{http_code}" $1
