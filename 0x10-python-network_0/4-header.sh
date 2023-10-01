#!/bin/bash
# send and display response
curl -d "X-School-User-Id=98" -X POST $1 | curl -sL $1
