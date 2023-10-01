#!/bin/bash
# send and display response
curl -d "X-School-User-Id=98" -X POST -sL $1
