#!/bin/bash
# Terraform workflow script
# Step 1: Initialize Terraform
terraform init

# Step 2: Apply changes automatically
terraform apply -auto-approve

# Step 3: Destroy resources
terraform destroy -auto-approve