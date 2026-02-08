# End-to-End AWS CI/CD Pipeline Portfolio Project, using Jenkins, Docker, and Terraform
---------------------------------------------------------------------------------------

This repository demonstrates a complete DevOps portfolio project showcasing an end-to-end CI/CD pipeline on AWS.

Note: The CI/CD pipelines are configured to run on GitLab. This GitHub repository is for portfolio demonstration purposes.

## Overview
- Jenkins CI/CD pipelines
- Docker containerization
- AWS infrastructure provisioned via Terraform
- End-to-end deployment to EC2 instances

## Folder Structure
- **architecture/** – Architecture diagrams for AWS setup
- **iac/terraform/** – Terraform scripts for provisioning AWS resources
- **ci-cd/** – Jenkinsfiles and pipeline scripts
- **app/** – Web application code
- **docker/** – Dockerfiles and container configurations
- **screenshots/** – Screenshots documenting setup and deployments

## Usage
- Users with `devops-admin` IAM account can run Terraform and manage resources via CLI
- Jenkins pipelines can be triggered to deploy the application end-to-end
