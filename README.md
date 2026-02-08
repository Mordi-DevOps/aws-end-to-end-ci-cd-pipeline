# End-to-End AWS CI/CD Pipeline Portfolio Project using Jenkins, Docker, and AWS services

This repository demonstrates a complete DevOps portfolio project showcasing an end-to-end CI/CD pipeline on AWS.

Note: The CI/CD pipelines are configured to run on GitLab. This GitHub repository is for portfolio demonstration purposes.

## Overview
The system automates the build, containerization, and deployment of a Flask-based web application using a Jenkins-driven CI/CD pipeline on AWS infrastructure.

## Architecture Flow

1. Developer pushes code to GitLab repository
2. Jenkins Controller triggers the CI/CD pipeline
3. Jenkins Agent performs build and test stages
4. Docker image is created
5. Image is pushed to Docker Hub
6. Web application is deployed to an AWS EC2 instance
7. Slack notifications are sent on pipeline success/failure

---

## Technologies Used

- Jenkins (CI/CD orchestration)
- Docker (containerization)
- AWS EC2 (infrastructure & deployment)
- GitLab (source control)
- Docker Hub (image registry)
- Slack (pipeline notifications)
- Flask (web application)

---

## Repository Structure

- **architecture/** – System design and architecture diagrams for AWS setup
- **iac/** – Infrastructure as Code (planned Terraform implementation)
- **ci-cd/** – Jenkins declarative pipeline configuration
- **WeatherApp/** – Python-Flask web application source code
- **docker/** – Docker build configuration
- **screenshots/** – Pipeline and infrastructure proof

---
## Notes and Usage

- CI/CD pipelines are configured to run from GitLab.
- Jenkins pipelines can be triggered to deploy the application end-to-end
- This GitHub repository serves as a public portfolio and documentation reference.

## Future Enhancements (Roadmap)

- Add VPC networking best practices: public/private subnets, Internet Gateway, and route tables
- Introduce an Application Load Balancer (ALB) with Target Groups and health checks for multi-instance web app deployment
- Provision infrastructure using Terraform (modules, remote state, and reusable components)
- Introduce monitoring and observability with metrics, alerts, dashboards (e.g., Prometheus, Grafana)
- Improve security posture (least privilege IAM roles, tighter security groups)

