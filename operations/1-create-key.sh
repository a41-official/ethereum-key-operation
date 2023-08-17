#!/bin/bash

# Set your withdrawal address and password
WITHDRAWAL_ADDRESS=""
PASSWORD=""

# Number of buckets to create
NUM_BUCKETS=3

# Loop to create buckets
for ((i=1; i<=NUM_BUCKETS; i++))
do
    FOLDER="./bucket-$(printf "%d" $i)"
    mkdir $FOLDER
    ./deposit new-mnemonic \
    --mnemonic_language 3 \
    --num_validators 250 \
    --folder $FOLDER \
    --chain goerli \
    --eth1_withdrawal_address $WITHDRAWAL_ADDRESS \
    --keystore_password $PASSWORD
    
    echo "Created bucket $i in folder $FOLDER"
done
