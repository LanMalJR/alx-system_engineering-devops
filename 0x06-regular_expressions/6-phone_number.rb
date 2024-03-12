#!/bin/bash

# Check if the argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <phone_number>"
    exit 1
fi

# Check if the phone number matches the regular expression
if [[ $1 =~ ^[[:space:]]*([0-9]{10})[[:space:]]*$ ]]; then
    echo "${BASH_REMATCH[1]}"
else
    echo "Invalid phone number"
fi
