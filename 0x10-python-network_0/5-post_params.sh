#!/bin/bash
#sends a POST , and displays the body of the response
curl -d "email='test@gmail.com'&subject='I will always be here for PLD'" -X POST -sL $1