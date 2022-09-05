#!/bin/bash

if [ ! -d .terraform ]; then
    terraform init
fi

terraform plan -out "terraform.tfplan"
terraform apply -auto-approve "terraform.tfplan"
